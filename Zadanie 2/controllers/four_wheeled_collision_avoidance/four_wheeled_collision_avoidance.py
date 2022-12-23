from controller import Robot

TIME_STEP = 64
robot = Robot()
ds = []
dsNames = ['ds_right', 'ds_left','colorSensor']
j = 2
for i in range(3):
    ds.append(robot.getDevice(dsNames[i]))
    ds[i].enable(TIME_STEP)
wheels = []
wheelsNames = ['Wheel1', 'Wheel2', 'Wheel3', 'Wheel4']
for i in range(4):
    wheels.append(robot.getDevice(wheelsNames[i]))
    wheels[i].setPosition(float('inf'))
    wheels[i].setVelocity(0.0)
avoidObstacleCounter = 0
while robot.step(TIME_STEP) != -1:
    leftSpeed = 1.0
    rightSpeed = 1.0
    if avoidObstacleCounter > 0:
        avoidObstacleCounter -= 1
        leftSpeed = 1.0
        rightSpeed = -1.0
    else:  # read sensors
       for i in range(2):   
            if ds[i].getValue() < 950.0 :
                avoidObstacleCounter = 0   
    if ds[j].getValue() > 900.0 :
        avoidObstacleCounter = 100 
        print(ds[j].getValue())      
    wheels[0].setVelocity(leftSpeed)
    wheels[1].setVelocity(rightSpeed)
    wheels[2].setVelocity(leftSpeed)
    wheels[3].setVelocity(rightSpeed)