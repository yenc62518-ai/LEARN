import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
x = np.array([1,2,3])
y = np.array([3,2,1])
z = pd.DataFrame({'x' : [1,2,3],
                 'y' : [4,5,6]})
plt.style.use('ggplot')
plt.plot(x,y, color = 'blue', label = 'x,y') 
plt.plot(z.x, z.y, color = 'red', label = 'z') #xz,yz, y(x)

#**********STYLE**********

#*********PYPLOT API************

plt.xlabel('x axis') 
plt.ylabel('y axis')
plt.title('test graph')
plt.legend()
plt.axis('tight')
plt.show()

#**********OO API**************
#1 Prepare data
plt.clf()
x = np.arange(0,10,2)
y = np.array([1,2,3,4,5])

#2 Setup plot
fig,ax = plt.subplots(figsize = (10,10)) # có thể không cần figsize
    # fig : đối tượng figure, toàn bộ khung chứa biểu đồ
    # ax : axes : vùng vẽ trong fig, nếu chỉ tạo 1 subplot thì ax là đối tượng Axes duy nhất
    # tạo nhiều subplot, có nghĩa là vẽ nhiều đồ thị hơn trong 1 figure
    # vd plt.subplot(2,2) thì ax là array chứa nhiều subplot

#3 Plot the data
ax.plot(x,y)

#4 Set data
ax.set(title = 'Test OOAPI',
       xlabel = 'x',
       ylabel = 'y')

plt.show()