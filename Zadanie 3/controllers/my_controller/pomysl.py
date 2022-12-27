"""labirynt controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
import numpy as np

MAZE_SIZE = 100
GRID_SIZE = 1

current_x = 50
current_y = 50
target_x = 9
target_y = 9

visited_grid = np.zeros((MAZE_SIZE, MAZE_SIZE))

# Oznacz początkowe miejsce jako odwiedzone
visited_grid[current_x][current_y] = 1

# Ustaw zmienne dotyczące kierunku poruszania się robota
direction = 0  # 0 - północ, 1 - wschód, 2 - południe, 3 - zachód

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = 32

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)
distance_sensors = []
for i in range(8):
    distance_sensors.append(robot.getDevice('ps' + str(i)))
    distance_sensors[i].enable(10)

leftMotor = robot.getDevice('left wheel motor')
rightMotor = robot.getDevice('right wheel motor')
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))
leftMotor.setVelocity(0.0)
rightMotor.setVelocity(0.0)
# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    while True:
        # Sprawdź, czy robot osiągnął cel
        if current_x == target_x and current_y == target_y:
            print("Cel został osiągnięty!")
            break

        # Pobierz odległości zmierzone przez czujniki odległości
        distances = []
        for i in range(8):
            distances.append(distance_sensors[i].getValue())

        # Sprawdź, czy przed robotem jest ściana
        wall_ahead = False
        for i in range(3):
            #print("Czujnik" +str(i) + " = " + str(distances[i]))
            if distances[i] > 80:
                wall_ahead = True
                break

        # Je
        if not wall_ahead:
            # Ustaw silniki robota na odpowiednią prędkość
            leftMotor.setVelocity(5.0)
            rightMotor.setVelocity(5.0)

            # Zwiększ aktualne współrzędne robota zależnie od kierunku poruszania się
            if direction == 0:
                current_y += 1
            elif direction == 1:
                current_x += 1
            elif direction == 2:
                current_y -= 1
            elif direction == 3:
                current_x -= 1

            # Oznacz aktualne miejsce jako odwiedzone
            #visited_grid[current_x][current_y] = 1
        else:
            # Jeśli przed robotem jest ściana, obróć się w lewo i spróbuj ponownie
            leftMotor.setVelocity(-5.0)
            rightMotor.setVelocity(5.0)

            # Zmień kierunek poruszania się robota
            direction = (direction - 1) % 4