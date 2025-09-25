'''Bài 2 – Xử lý mảng 2D
Yêu cầu:
Sinh ma trận ngẫu nhiên 10×5 chứa giá trị nhiệt độ (°C) từ 20 → 40.
Tìm
Nhiệt độ cao nhất ở mỗi cột.
Hàng có trung bình nhiệt độ cao nhất.
Chuyển đổi đơn vị từ °C sang °F:'''
import numpy as np
temp = np.random.randint(20,40, [10,5])
print(temp, '\n \n*******\n')
max_temp = np.max(temp, axis = 1)
print(max_temp)
row_mean = np.mean(temp, axis = 0) 
print(row_mean)
max_temp_id = np.argmax(row_mean)
print(max_temp_id)
#print (f"hang {max_id} co nhiet do trung binh cao nhat : {max_temp}")
    
