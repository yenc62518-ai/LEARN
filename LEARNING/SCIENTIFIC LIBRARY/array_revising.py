import numpy as np
'''Lấy hàng thứ 2.
Lấy cột cuối.
Lấy các phần tử từ hàng 1 đến hàng 2, cột 2 đến cột 4.'''
arr = np.arange(1, 13).reshape(3, 4)
print(arr )
print(arr[1])
print(arr[: , -1:])
print(arr[0:2,1:3])
print("\n\n*********\n\n")
'''Cộng a vào từng hàng của b bằng broadcasting.

Tính a * b và giải thích vì sao vẫn chạy được.'''
a = np.array([1, 2, 3])
b = np.array([[10],
              [20],
              [30]])
print(a+b)
print(a*b)
print("\n\n ********* \n\n")

'''Tạo mảng data gồm 100 giá trị ngẫu nhiên trong khoảng [0, 50].

Tính giá trị trung bình, độ lệch chuẩn.

Lọc ra các giá trị lớn hơn 40.'''
np.random.seed(0)
rd = np.random.randint(0, 50, size = 100)
rd.reshape(5,20)
print(rd)
print(f"standard deviation {np.std(rd)}, avg value {np.mean(rd)}")
mask = rd<40
rd[mask]
rd[rd<40] = 0
print(rd, "\n\n *********\n")

'''Tạo mảng m 4×3 từ np.arange(12).

Reshape thành 3×4.

Flatten mảng này thành 1 chiều.

Transpose và so sánh với mảng ban đầu.'''

m = np.arange(1,13, dtype='int32').reshape(4,3)
m.reshape(3,4)
print(m,'\n')
m=m.flatten() #trả về mảng 1 chiều
print(m, '\n\n **********\n')

'''Giả sử bạn có ma trận cảm biến 10×5, mỗi hàng là dữ liệu từ một lần đo, mỗi cột là giá trị của một cảm biến:

Tính trung bình và độ lệch chuẩn của từng cảm biến.

Chuẩn hóa dữ liệu (z-score).

Lọc ra các hàng có giá trị cảm biến số 2 vượt quá 1.5 lần độ lệch chuẩn.'''
random = np.random.randint(1, 100, size = 50).reshape(10,5)
print(random)
z_score = []
for it in range (5) :
    print(random[ : , it])
    part = []
    std = np.std(random[ : , it])
    mean = np.mean(random[ : , it])
    for i in random[ : , it] :
        part.append(float((i-mean)/std))
    z_score.append(part)
mean = np.mean(random[ : , 1])
print('mean = ',mean)
for i in random[ : , 1] :
    if (i > mean+std*1.5) :
        print(f"thoi diem {i} \n")
#z_score giờ là 1 list chứa 5 list, mỗi list con là z score cho mỗi cảm biến
#nếu yêu cầu tìm hàng có cảm biến số 2 > 1,5 tức yêu cầu tìm thời điểm list con số 2 lỗi giá trị
#tức quét qua i 