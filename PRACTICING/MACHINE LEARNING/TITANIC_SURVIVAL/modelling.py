import pandas as pd
import numpy as np

train_set = pd.read_csv('./train.csv')
test_set = pd.read_csv('./test.csv')
PID = test_set['PassengerId']
features = ['Age',"Pclass", "Sex", "SibSp", "Parch", 'Cabin', 'Fare', 'Embarked']
train = train_set[features]
test = test_set[features]
train['Fare'] = np.log1p(train['Fare'])
test['Fare'] = np.log1p(test['Fare'])
train['Cabin'] = train['Cabin'].str[0]
test['Cabin'] = test['Cabin'].str[0]
train = pd.get_dummies(train, columns=['Embarked','Cabin'], drop_first=True)
test = pd.get_dummies(test, columns=['Embarked','Cabin'], drop_first=True)
train, test = train.align(test, join="left", axis=1, fill_value=0)
print(train.head())

from sklearn.impute import SimpleImputer
SI = SimpleImputer(strategy='mean')
train['Age'] = SI.fit_transform(train[['Age']])
test['Age'] = SI.fit_transform(test[['Age']])

from sklearn.preprocessing import LabelEncoder
LE = LabelEncoder()
train['Sex'] = LE.fit_transform(train['Sex'])
test['Sex'] = LE.transform(test['Sex']) # chỉ fit cho train, sau đó transform cho cả 2 để giữ cùng không gian

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(train, train_set['Survived'], train_size=0.8, random_state=42)
print(x_train.head())
print(y_train.head())

from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
DTC = DecisionTreeClassifier() 
DTC.fit(x_train, y_train)
sur_pred = DTC.predict(x_test)
acc = accuracy_score(y_test, sur_pred)
print(f"Decision Tree : {acc}")

from sklearn.ensemble import RandomForestClassifier
RFC = RandomForestClassifier(
    n_estimators=100, 
    max_depth=10, 
    random_state=42
)
RFC.fit(x_train, y_train)
sur_pred = RFC.predict(x_test)
result = pd.DataFrame({'Reality' : y_test,
                       'Predicted' : sur_pred})


acc = accuracy_score(y_test, sur_pred)
print("Accuracy of RandomForest:", acc)
print("Error rate:", 1 - acc)


predictions = RFC.predict(test)

output = pd.DataFrame({'PassengerId': PID, 'Survived': predictions})
output.to_csv('submission.csv', index=False)
print("Your submission was successfully saved!")
