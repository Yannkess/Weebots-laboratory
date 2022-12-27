class Control:
    def __init__(self,leftWheelSensor):
        self.leftWheelSensor = leftWheelSensor

    def turn(self,where):
        startMeasure = 0
        MAX_SPEED = 3
        angle = 2.1
        if startMeasure == 0:
                startLeftWheelSens = self.leftWheelSensor
                startMeasure = 1
        if where == 1:
            leftSpeed  = MAX_SPEED
            rightSpeed = -MAX_SPEED
            leftWheelSens = self.leftWheelSensor
            if leftWheelSens - startLeftWheelSens >= angle:
                print("Dokonano obrotu o 90 stopni")
                return leftSpeed,rightSpeed
        elif where == 2:
            leftSpeed  = MAX_SPEED
            rightSpeed = -MAX_SPEED
            leftWheelSens = self.leftWheelSensor
            if leftWheelSens - startLeftWheelSens >= 2*angle:
                print("Dokonano obrotu o 180 stopni")
                return leftSpeed,rightSpeed
        elif where == 3:
            leftSpeed  = -MAX_SPEED
            rightSpeed = MAX_SPEED
            leftWheelSens = self.leftWheelSensor
            if leftWheelSens - startLeftWheelSens <= -2*angle:
                print("Dokonano obrotu o -180 stopni")
                return leftSpeed,rightSpeed
        elif where == 4:
            leftSpeed  = -MAX_SPEED
            rightSpeed = MAX_SPEED
            leftWheelSens = self.leftWheelSensor
            if leftWheelSens - startLeftWheelSens <= -angle:
                print("Dokonano obrotu o -90 stopni")
                return leftSpeed,rightSpeed

       