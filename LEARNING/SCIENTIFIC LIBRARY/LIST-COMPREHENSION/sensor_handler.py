import numpy as np
import csv
data = []
with open (r'D:\Code C\VS\PRACTICE\NUMPY\sensor_data.csv', 'r', encoding = 'utf-8') as data_csv :
    contents = csv.reader(data_csv)
    next(contents)
    for each in contents :
        data.append(float(each[0]))
data = np.array(data, dtype = float) 
print ('do lech chuan',np.std(data))
print ('gia tri trung binh',np.mean(data))