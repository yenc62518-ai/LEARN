'''Bài 1 – NumPy cơ bản
Tạo mảng NumPy arr gồm 100 số ngẫu nhiên từ 0 → 100.
Tính:
Giá trị trung bình và độ lệch chuẩn.
Các phần tử lớn hơn (mean + std).
Chuẩn hóa dữ liệu (z-score):
'''
import numpy as np
arr = np.random.randint(0,101,size = 100) 
mean = np.mean(arr) 
std = np.std(arr) 
cnt = [x for x in arr if x>(mean+std)]
z_score = [(x-mean)/std for x in arr]
print(z_score)
