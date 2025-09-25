import csv

class Hocsinh :
    def __init__(self, name, age, code) :
        self.name = name
        self.age = int(age)
        self.code = code
    @classmethod #factory method, giúp khởi tạo đối tượng cho class
    def initialize(cls, row) :
        return cls(row['name'], row['age'], row['code']) #khi được gọi đến, sẽ trã lại 1 đối tượng mang các thuộc tính như được cài đặt

students = []

with open('D:\Code C\VS\LEARNING\Factory_method_learn\danh_sach.csv', 'r', encoding = 'utf-8') as f :
    content = csv.DictReader(f)
    for each in content :
        hs = Hocsinh.initialize(each)
        students.append(hs)

def find(name) :
    for each in students :
        if each.name == name :
            return each.age, each.code

tuoi, lop = find(input()) 
print(f"tuoi la {tuoi} lop la {lop}")
