import csv

class Sensor :
    def __init__(self, id, value, status):
        self.id = id
        self.value = float(value)
        self.status = status
    @classmethod
    def create(cls, id, value, status) :
        return cls(id, value, status)
     
class SensorManager :
    def __init__ (self) :
        self.sensor_list = []
    def read_csv(self) :
        with open ("D:\Code C\VS\PRACTICE\MINI_PROJECT\sensor.csv", 'r') as csv_file :  
            self.sensor_list.clear()
            contents = csv.DictReader(csv_file)
            for each in contents :
                if float(each['value']) >= 30 :
                    each['status'] = "warning"
                elif float(each['value']) < 0 :
                    each['status'] = "error"
                else : 
                    each['status'] = "normal"
                sensor = Sensor(each['id'], each['value'], each['status'])
                self.sensor_list.append(sensor)   
    def print_all(self) :
        for each in self.sensor_list :
            print(f"{each.id} - {each.value} - {each.status}")
    def add(self, id) :
        self.sensor_list.append(id, 0, 'no operation')
    def avg_calc(self) :
        total_sum = 0
        for ite in self.sensor_list :
            total_sum += ite.value
        print(total_sum/len(self.sensor_list))


def menu():
    manager = SensorManager()
    manager.read_csv()
    while True:
        print("\n=== SENSOR MANAGER ===")
        print("1. Đọc dữ liệu từ CSV")
        print("2. In danh sách cảm biến")
        print("3. Thêm cảm biến")
        print("5. Tính giá trị trung bình")
        print("6. Tìm cảm biến bất thường")
        print("7. Lưu danh sách ra CSV")
        print("0. Thoát")
        choice = input("Chọn chức năng: ")

        match choice:
            case '1':
                manager.read_csv()
                print("✅ Đã đọc dữ liệu.")
            case '2':
                manager.print_all()
            case '3' :
                id = int(input('nhap id'))
                for ite in manager.sensor_list :
                    if ite.id==id :
                        print('id da ton tai') 
                        break
                    else :
                        manager.add(id)
            case '4' :
                manager.avg_calc()
menu()


