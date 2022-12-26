from controller import Robot
from pid_controller import PIDController
from sensor_output import SensorReading
speed = 2
detected = 0
TIME_STEP = 64
robot = Robot()
pid_controller = PIDController(kp=0.005, ki=0, kd= 0.0001, setpoint=3000, min_output=-2*speed, max_output=2*speed)
sensorReader = SensorReading(0,0,0,0,0)
ds = []
dsNames = ['ds_right', 'ds_left','cs_1','cs_2','cs_3','cs_4','cs_5']
for i in range(7):
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
    leftSpeed = speed
    rightSpeed = speed
    leftds = ds[0].getValue()
    rightds = ds[1].getValue()
    sensorReader.sensor1  = ds[2].getValue()
    sensorReader.sensor2  = ds[3].getValue()
    sensorReader.sensor3  = ds[4].getValue()
    sensorReader.sensor4  = ds[5].getValue()
    sensorReader.sensor5  = ds[6].getValue()
    sensorOutput = sensorReader.update()
    output = pid_controller.update(sensorOutput)
    print ("sensor1 = " + str(sensorReader.sensor1))
    print ("sensor2 = " + str(sensorReader.sensor2))
    print ("sensor3 = " + str(sensorReader.sensor3))
    print ("sensor4 = " + str(sensorReader.sensor4))
    print ("sensor5 = " + str(sensorReader.sensor5))
    print ("sensorOutput = " + str(sensorOutput))
    print ("Output = " + str(output))

    if output > 0:
        wheels[0].setVelocity(leftSpeed)
        wheels[1].setVelocity(rightSpeed - output)
        wheels[2].setVelocity(leftSpeed)
        wheels[3].setVelocity(rightSpeed - output)
    elif output < 0:
        wheels[0].setVelocity(leftSpeed + output)
        wheels[1].setVelocity(rightSpeed)
        wheels[2].setVelocity(leftSpeed + output)
        wheels[3].setVelocity(rightSpeed)
    else:
        wheels[0].setVelocity(leftSpeed)
        wheels[1].setVelocity(rightSpeed)
        wheels[2].setVelocity(leftSpeed)
        wheels[3].setVelocity(rightSpeed)
