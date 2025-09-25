import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import SimpleImputer

def missing_plot(data) : #vẽ heatmap missing data
    fig, ax = plt.subplots()
    sns.heatmap(data=data.isna(), cmap = 'Blues')
    plt.show()

def purchase_percent(x, y):
    x = pd.DataFrame(x, columns=['Country', 'Age', 'Salary']) #do x sau khi iloc.values trở thành dạn array
    data = x.copy()
    data['Purchase'] = pd.Series(y, index = x.index) #gán y vào mỗi hàng của x
    print(data.head()) #lúc này data là dataframe hoàn chỉnh (đề cho)
    data["Purchased"] = pd.Series(y, index=x.index)
    pvt = data.pivot_table (
        values = 'Purchased',
        index="Salary",
        columns="Age",
        aggfunc="mean")
    plt.figure()
    sns.heatmap(pvt, cbar=False)
    plt.show()


data_df = pd.read_csv('./Data.csv')
print(data_df.head())

#*********DATA IMPUTATION - MISSING DATA REPLACEMENT***********

data_df.info() #10 rows, with 2 rows having 1 null - NaN value
for col in data_df :
    missing = data_df[col].isna().sum() #isna trả về true/false ứng với mỗi row, sum trả về tổng số lượng isna là true
    print(f"missing data percentage : {missing/len(data_df)*100}%")
print(data_df['Age'].isna().sum()) # in tổng số lượng missing data

x = data_df.iloc[:, 0:-1].values #hàm values mang dữ liệu dạng dataframe thành mảng array (array chứa array)
y = data_df.iloc[:,(-1)].values
# y : giá trị phụ thuộc, kiểu DL array

#********* IMPORT SCIKIT LEARN SIMPLE IMPUTER - XỬ LÝ MISSING DATA *************

imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean') #đây là setup Simple Imputer, áp dụng khi gọi hàm 
x[:, 1:3] = imputer.fit_transform(x[:,1:3]) 

#********* ENCODE CATEGORICAL DATA - MÃ HÓA DỮ LIỆU DANH MỤC *************
#***** COLUMN TRANSFORMER - XỬ LÝ DỮ LIỆU DANH MỤC (KHÁC SỐ) *******
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
ct = ColumnTransformer(transformers = [('encoder', OneHotEncoder(), [0])], remainder='passthrough')
X = ct.fit_transform(x)
# giải thích : 'encoder' - đặt tên cho bước encode để quản lý, gọi
# OneHotEncoder() : method dùng để encode
# [0] : dữ liệu cục bộ của biến cần encode, ở đây cột [0] của parameter truyền vào ct sẽ được encode bằng OneHotEncoder


#*** LABEL ENCODER - XỬ LÝ DANH MỤC DẠNG YES/NO ***

le = LabelEncoder()
y = le.fit_transform(y)
#y từ yes no sang 1 0

#************* MACHINE LEARNING ***************
#******* train_test_split - CHIA THÀNH TRAINING SET VÀ TESTING SET **********
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X,y, train_size=0.8)

#******* FEATURE SCALING - CO DÃN DỮ LIỆU ********
from sklearn.preprocessing import StandardScaler
SC = StandardScaler() # initiate đối tượng SC
x_train[:, 3:] = SC.fit_transform(x_train[:, 3:]) # chỉ featuring cột 3 và 4 tức age và salary
x_test[:, 3:] = SC.transform(x_test[:, 3:])