import numpy as np
import csv
with open (r'D:\Code C\VS\PRACTICE\NUMPY\control_system.csv', 'r') as data_csv :
    contents = csv.reader(data_csv) 
    data = []
    data = [list(map(float, row)) for row in contents]
    '''
    duyệt từng row là list chứa các thông số trong contents, chuyển list trên thành
    float qua map(function, argument), hàm trên sẽ trả về 1 map object, chuyển map 
    object trên thành list (map object là dạng dữ liệu đặc biệt), lúc này list sẽ
    chứa dữ liệu float trên, sau đó toàn bộ cac list đã được convert sang float, sẽ
    được thêm vào 1 list chứa list khác qua [] (list comprehension) và gắn vào data
    '''
data = np.array(data)
system, ampl = (np.split(data, [3], axis = 0))
print(system.T.dot(ampl.T))