import csv

class sensor :
    def __init__(self, name, type, time) :
        self.name = name
        self.time = time
        self.type = type

    def read(self) :
        with open ("D:\\Code C\\VS\\StudyOOP\\sensor_data.csv", 'r') as sensor_data :
            sensor_reader = csv.reader(sensor_data)
            next(sensor_reader)
            for line in sensor_reader :
                if (line[0]==self.name and line[1] == self.type and line[2] == self.time) :
                    return line[3]
        return None 

sensor_check = sensor("S001", "Temperature", "2025-07-28 08:13:00")
print(sensor_check.read())
