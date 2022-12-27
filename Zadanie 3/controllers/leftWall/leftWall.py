from controller import Robot
import numpy as np


MAZE_SIZE = 5000
GRID_SIZE = 1
current_x = 2500
current_y = 2500
visited_grid = np.zeros((MAZE_SIZE, MAZE_SIZE))
visited_grid[current_x][current_y] = 1
direction = 1

TIME_STEP = 32
angle = 2.099
MAX_SPEED = 3
robot = Robot()
ps = []
psNames = [

    'ps0', 'ps1', 'ps2', 'ps3',
    'ps4', 'ps5', 'ps6', 'ps7'
]

for i in range(8):
    ps.append(robot.getDevice(psNames[i]))
    ps[i].enable(TIME_STEP)

leftMotor = robot.getDevice('left wheel motor')
rightMotor = robot.getDevice('right wheel motor')
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))
leftMotor.setVelocity(0.0)
rightMotor.setVelocity(0.0)
leftWheelSensor = robot.getDevice('left wheel sensor')
leftWheelSensor.enable(TIME_STEP)
robotir = robot.getDevice('ir0')
robotir.enable(TIME_STEP)


turn = 0
startMeasure = 0
startMeasure1 = 0
startMeasure2 = 0
turned = 0
startRotation = 0
turning = 0 
finish = 0
######################################################################################################################
while robot.step(TIME_STEP) != -1:

    # read sensors outputs
    psValues = []
    for i in range(8):
        psValues.append(ps[i].getValue())
    leftWheelValue = leftWheelSensor.getValue()
    robotirValue = robotir.getValue()

    if psValues[5] > 80:
        turned = 0
        startRotation = 0

    if (psValues[0] > 120 or psValues[7] > 120) and psValues[5] > 120 and turn == 0 and visited_grid[current_x][current_y] == 0 and turning == 0 and finish == 0:
        turn = 1
    elif (psValues[0] > 120 or psValues[7] > 120) and psValues[5] < 120 and turn == 0 and visited_grid[current_x][current_y] == 0 and turning == 0 and finish == 0:
        turn = 1
    elif(psValues[0] > 120 or psValues[7] > 120) and psValues[5] < 120 and turn == 0 and visited_grid[current_x][current_y] == 1 and turning == 0 and finish == 0:
        turn = 4
    elif (psValues[5] < 120 or psValues[7] < 120) and psValues[5] < 65 and turn == 0 and finish == 0:
        if startMeasure1 == 0:
                startLeftWheelSens1 = leftWheelValue
                startMeasure1 = 1
        if leftWheelValue - startLeftWheelSens1 >= 2 and turned == 0 and visited_grid[current_x][current_y] == 0 and turning == 0:
                turn = 4
                startRotation = 1
        elif leftWheelValue - startLeftWheelSens1 >= 2 and turned == 0 and visited_grid[current_x][current_y] == 1 and turning == 0:
            turn = 1
            startRotation = 1 
        if leftWheelValue - startLeftWheelSens1 <= (10 - angle) and startRotation == 1:
            turned = 1
            startMeasure1 = 0

    if finish == 1:
        turn = 5
        print("Pomyślnie wyjechane z labiryntu") 
        leftSpeed = 0
        rightSpeed = 0  
    if turn == 0 and finish == 0:
        leftSpeed  = 0.5* MAX_SPEED
        rightSpeed = 0.5* MAX_SPEED
        if startMeasure2 == 0:
                startLeftWheelSens2 = leftWheelValue
                startMeasure2 = 1 
        if leftWheelValue - startLeftWheelSens2 >= 1:
            print("Current x = " + str(current_x))
            print("Current y = " + str(current_y))
            visited_grid[current_x][current_y] = 1
            if direction == 1:
                    current_y += 1
            elif direction == 2:
                    current_x += 1
            elif direction == 3:
                    current_y -= 1
            elif direction == 4:
                    current_x -= 1
            startMeasure2 = 0
            if robotirValue > 11:
                finish = 1     
                    

    elif turn != 0 and finish == 0:

        if startMeasure == 0:
                startLeftWheelSens = leftWheelValue
                startMeasure = 1
                turning = 1
        if turn == 1:
            leftSpeed  = MAX_SPEED
            rightSpeed = -MAX_SPEED
            leftWheelSens = leftWheelValue
            if leftWheelSens - startLeftWheelSens >= angle:
                startMeasure = 0
                turn = 0
                turning = 0
                if direction < 4:
                    direction += 1
                else:
                    direction = 1
            
        elif turn == 2:
            leftSpeed  = MAX_SPEED
            rightSpeed = -MAX_SPEED
            leftWheelSens = leftWheelValue
            if leftWheelSens - startLeftWheelSens >= 2*angle:
                startMeasure = 0
                turn = 0
                turning = 0
                if direction < 3:
                    direction += 2
                elif direction == 3:
                    direction = 1
                elif direction == 4:
                    direction = 2
                
        elif turn == 3:
            leftSpeed  = -MAX_SPEED
            rightSpeed = MAX_SPEED
            leftWheelSens = leftWheelValue
            if leftWheelSens - startLeftWheelSens <= -2*angle:
                startMeasure = 0
                turn = 0
                turning = 0
                if direction > 2:
                    direction -= 2
                elif direction == 2:
                    direction = 4
                elif direction == 1:
                    direction = 3

        elif turn == 4:
            leftSpeed  = -MAX_SPEED
            rightSpeed = MAX_SPEED
            leftWheelSens = leftWheelValue
            if leftWheelSens - startLeftWheelSens <= -angle:
                startMeasure = 0
                turn = 0
                turning = 0
                if direction > 1:
                    direction -= 1
                else:
                    direction = 4


  

  
    leftMotor.setVelocity(leftSpeed)
    rightMotor.setVelocity(rightSpeed)