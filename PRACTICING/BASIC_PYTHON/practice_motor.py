'''	
Nội dung: 
o	Tạo thuộc tính và phương thức trong class.
o	Ứng dụng: Quản lý trạng thái thiết bị hoặc tính toán thông số.
•	Bài tập: 
o	Tạo class Motor với thuộc tính (tên, công suất, trạng thái) và phương thức tính năng lượng tiêu thụ (công suất * thời gian)
'''
class System :
    def __init__(self) :
        self.motor_system = []
    def add_motor(self, motor) :
        self.motor_system.append(motor)
    def find_motor(self, name) :
        for each in self.motor_system :
            if each.name == name :
                return each.power
    def show(self) :
        for each in self.motor_system :
            print(each.name +" : "+ str(each.power))
    
class Motor :
    def __init__(self, name, power, state) :
        self.name = name
        self.power = power
        if (state=="ON" or state=="OFF") :
            self.state = state
        else :
            print ("given state is not valid")

    def power_consumed(self, time) :
        if self.state == "ON" :
            return self.power*time
        elif self.state == "OFF" :
            return 0

system1 = System()
system1.add_motor(Motor("M001", 2000, "ON"))
system1.add_motor(Motor("M002", 2000, "ON"))
system1.add_motor(Motor("M003", 2000, "OFF"))
system1.show()