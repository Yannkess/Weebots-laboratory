from controller import Robot
detected = 0
TIME_STEP = 64
robot = Robot()
ds = []
dsNames = ['ds_right', 'ds_left','colorSensor']
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
    leftSpeed = 2.0
    rightSpeed = 2.0
    leftds = ds[0].getValue()
    rightds = ds[1].getValue()
    colSens = ds[2].getValue()
    if detected == 1:
        print("left ds = " + str(leftds))
        print("right ds = " + str(rightds))
        if leftds >= 1000 and rightds >= 500:
            leftSpeed = -2
            rightSpeed = 2
        elif rightds >= 1000 and leftds >= 500:
            leftSpeed = 2
            rightSpeed = -2
        else:
            leftSpeed = 2.0
            rightSpeed = 2.0
    elif detected == 0:
        if avoidObstacleCounter > 0:
            avoidObstacleCounter -= 1
            leftSpeed = -1.0
            rightSpeed = 1.0     
        else:  # read sensors
            for i in range(2):   
                    if ds[i].getValue() < 550.0 :
                        detected = 1                   
    if colSens > 900.0:
          avoidObstacleCounter = 100 
          detected = 0
    print("Detected = " + str(detected))
    wheels[0].setVelocity(leftSpeed)
    wheels[1].setVelocity(rightSpeed)
    wheels[2].setVelocity(leftSpeed)
    wheels[3].setVelocity(rightSpeed)