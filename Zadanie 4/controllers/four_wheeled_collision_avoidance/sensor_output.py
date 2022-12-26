from audioop import avg

class SensorReading:
    def __init__(self, sensor1, sensor2, sensor3, sensor4, sensor5):
        self.sensor1 = sensor1
        self.sensor2 = sensor2
        self.sensor3 = sensor3
        self.sensor4 = sensor4
        self.sensor5 = sensor5

    def update(self):
    
        output = 3000

        if self.sensor3 > 730:
           #output += self.sensor3*3
           output = 3000
        elif self.sensor2 > 730 and self.sensor3 < 730 :
            #output += self.sensor2*2
            output = 2000
        elif self.sensor1 > 730 and self.sensor3 < 730 and self.sensor2 < 730:
            #output += self.sensor1
            output = 1000
        elif self.sensor4 > 730 and self.sensor3 < 730:
            #output += self.sensor4*4
            output = 4000
        elif self.sensor5 > 730 and self.sensor3 < 730 and self.sensor4 < 730:
           #output += self.sensor5*5
           output = 5000
    

        avgSensor = (self.sensor1 + self.sensor2 + self.sensor3 + self.sensor4 + self.sensor5)/5
        
        return output