class Equipment :
    def __init__(self, name, serial_number) :
        self.name = name
        self.__serial_number = serial_number
    def __str__(self) :
        return f"ten {self.name} - ma so {self.__serial_number}"
robot = Equipment("robot", "001") 
servo = Equipment("servo", "002") 
print (robot)
print (servo)       