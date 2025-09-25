import pandas as pd 
import numpy as np

def statistic(arr) :
    return np.mean(arr), np.max(arr), np.min(arr)

data = pd.read_csv("mtcars-parquet.tsv", sep = '\t') 
print (data.tail(5))
data.info()
miss_data = data.isna().sum().sum() #kiem tra so cot bi thieu, sum đầu tiên là của từng cột, sum 2 là cho toàn bảng
mpg = np.array(data['mpg'])
mean_mpg, max_mpg, min_mpg = statistic(mpg)
print (f"mean : {mean_mpg}, max : {max_mpg}, min : {min_mpg}")

#sorting
mpg_25 = data.loc[(data.mpg > 25), ['model', 'mpg']]
cyl4_hp100 = data.loc[((data.cyl == 4) & (data.hp < 100)), ['model', 'cyl', 'hp']]
gear5_carb4 = data.loc[((data.gear == 5) | (data.carb>=4)), ['model', 'gear', 'carb']]

#thêm cột
data['kmL'] = data['mpg'] * 0.425144 
data["weight_kg"] = data["wt"] * 453.592
print (data)

#groupby and statistical working
print(data.groupby('cyl')['mpg'].mean()) #tính trung bình mpg theo từng nhóm cyl.
print(data.groupby('gear')['hp'].mean()) #Tính công suất trung bình (hp) cho từng số gear.
print(data.value_counts('am')) #Đếm số xe trong mỗi nhóm am (0 = số tự động, 1 = số tay).

#count_values & nunique
print(f'nunique : {data['carb'].nunique()} \n value_counts() : {data['carb'].value_counts()}')
#nunique : chỉ trả về số lượng số phần tử khác nhau, value_counts trả về từng phần tử khác nhau 
#và số lần xuất hiện

#ordering
#Sắp xếp xe theo mpg giảm dần.
print(data.sort_values(by=['mpg'], ascending = False)[['model', 'mpg']])