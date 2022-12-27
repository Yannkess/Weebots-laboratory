from controller import Robot


TIME_STEP = 32
angle = 2.1
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

turn = 0
startMeasure = 0
######################################################################################################################
while robot.step(TIME_STEP) != -1:
    # read sensors outputs
    psValues = []
    for i in range(8):
        psValues.append(ps[i].getValue())
    leftWheelValue = leftWheelSensor.getValue()
    ###############################################################################################################
    leftSpeed  = 0.5 * MAX_SPEED
    rightSpeed = 0.5 * MAX_SPEED

    if (psValues[0] > 150 or psValues[7] > 150) and psValues[5] > 120 and turn == 0:
        turn = 1
    elif (psValues[0] > 150 or psValues[7] > 150) and psValues[2] > 120 and turn == 0 :
        turn = 2
    elif (psValues[0] > 150 or psValues[7] > 150) and turn == 0:
        turn = 1
    if turn == 1 or turn == 2:
        #print("turn = " + str(turn))
        if startMeasure == 0:
            startLeftWheelSens = leftWheelValue
            startMeasure = 1
        if turn == 1:
            leftSpeed  = MAX_SPEED
            rightSpeed = -MAX_SPEED
        elif turn == 2:
            leftSpeed  = -MAX_SPEED
            rightSpeed = MAX_SPEED
        leftWheelSens = leftWheelValue
        print("Roznica  = " + str(leftWheelSens - startLeftWheelSens))
        if leftWheelSens - startLeftWheelSens >= angle or leftWheelSens - startLeftWheelSens <= -angle:
            print("Dokonano obrotu o 90 stopni")
            turn = 0
            startMeasure = 0
  
    # write actuators inputs
    leftMotor.setVelocity(leftSpeed)
    rightMotor.setVelocity(rightSpeed)