import csv
class Device : 
    def stop(self) :
        print("thiet bi chua bat nguon")
    def __init__ (self, type, id, status = "OFF") :
        self.type = type
        self.id = id
        self.status = status 
        if status=="OFF" :  
            self.stop()
        
class Robot(Device) :
    def __init__ (self, type, id, status, location) :
        super().__init__(type, id, status) 
        self.location = location
    
    def move(self, direction) :
        if self.status == "ON" :
            match (direction) :
                case "forward" :
                    print('move forward')
                case "backward" :
                    print('move backward')
    def stop_robot(self) :
        print ("stop")
        self.status = "OFF" 
    def get_location(self) :    
        return self.location

class Servo(Device) :
    def __init__(self, type, id, status, angle) :
        super().__init__(type, id, status="OFF") 
        self.angle = angle
    def rotate(self) :
        print(f"rotate to {self.angle} degree")

class Sensor(Device) :
    def read_data(self) :
        with open ('D:\Code C\VS\PRACTICE\INHERITANCE_PRATICE\sensor_data.csv', 'r') as f :
            f_read = csv.reader(f) 
            for each in f_read :
                return each[1] #cho rang cot thu 2 la gia tri sensor

