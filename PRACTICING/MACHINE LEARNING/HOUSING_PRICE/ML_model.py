import pandas as pd
import numpy as np

data = pd.read_csv('./train.csv', index_col = ['Id'])
feature = ['MSSubClass','MSZoning','Electrical','SaleType','YrSold','TotRmsAbvGrd','Street','LotArea','HouseStyle','YearBuilt','KitchenQual','GarageArea','Neighborhood', 'OverallQual','OverallCond','SaleCondition']
OH = ['MSSubClass','Electrical','MSZoning','Street','SaleType','HouseStyle','KitchenQual','Neighborhood','SaleCondition']
X = data[feature]
Y = data['SalePrice']

from sklearn.impute import SimpleImputer
num_cols = X.drop(columns=OH).columns
SI = SimpleImputer(strategy='mean')
X.loc[:, num_cols] = SI.fit_transform(X[num_cols])

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
CT = ColumnTransformer(transformers = [('encoder', OneHotEncoder(), OH)], remainder='passthrough')
X = CT.fit_transform(X)

from sklearn.model_selection import  train_test_split
x_train, x_test,y_train, y_test = train_test_split(X,Y, train_size=0.8, random_state=0)

from sklearn.tree import DecisionTreeRegressor 
DT = DecisionTreeRegressor()
DT.fit(x_train, y_train) 
y_pred = DT.predict(x_test)
prediction_check = pd.DataFrame({'real' : y_test, 'predict' : y_pred})
prediction_check['error'] = abs(prediction_check['real'] - prediction_check['predict']) / prediction_check['real'] * 100
print(np.mean(prediction_check['error']))
from sklearn.ensemble import RandomForestRegressor
RFR = RandomForestRegressor(
    n_estimators=100, 
    max_depth=10, 
    random_state=42
)
RFR.fit(x_train, y_train)
rs_pred = RFR.predict(x_test)
prediction_check['real']=y_test
prediction_check['predict'] = rs_pred
prediction_check['error'] = abs(prediction_check['real'] - prediction_check['predict']) / prediction_check['real'] * 100
print(np.mean(prediction_check['error']))
# giả sử dataframe tên là df
prediction = pd.Series()
prediction.to_csv("ten_file.csv", index=False, encoding="utf-8")
print(y_test.head())
print(rs_pred[:5])

