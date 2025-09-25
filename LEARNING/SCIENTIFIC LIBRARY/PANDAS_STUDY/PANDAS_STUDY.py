import pandas as pd 
import numpy as np

titanic = pd.read_csv('titanic-parquet.tsv', sep = '\t') 
print(titanic.head(10)) #print first 10 rows
print(titanic.shape) #print its shape
print(titanic.info()) #print each column's information
print(list(titanic.columns)) #print columns's name
print(titanic.describe()) #print statistical information of numeric columns
x = titanic.iloc[0:11,1:5]
print(x)
print(titanic.Name[:5]) #print the first 5 names (only names)
print(titanic['Name'][:5]) #have the same function as above
cnt = 0
print(titanic['Fare'].sum()) #total sum 
titanic.groupby('Survived')['Name'] #nhóm các hành khách sống và chết thành 2 dataframe
fare = titanic.groupby('Name')['Fare'].sum()
titanic['Fare'].apply(lambda x : float(x))
fare = fare.sort_values(ascending = False) 
print (fare.head(5))
print(titanic.Sex.value_counts()) #count số lượng nam và nữ (các value khác nhau của cột được value count)
print(titanic.Sex.nunique())