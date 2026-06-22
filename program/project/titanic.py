import pandas as pd 
import numpy as np 


df = pd.read_csv("./titanic.csv")
print(df.tail())
print(df['Age'].dtype)
print(df['Age'].apply(type).value_counts())


data = {0:"not survivd",1:"survived"}
df['Survived'] = df['Survived'].map(data)
print(df)

df.shape
print(df.describe())

print(df.info())

from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
df['Sex'] = encoder.fit_transform(df['Sex'])
print(df.head())

print(df.head(10))

df.isnull().sum()

df['Age'] = df["Age"].fillna(df['Age'].median())

print(df.tail(5))
print(df.info())

df.drop(['Embarked','Cabin','Ticket'], axis=1, inplace=True)
print(df.info)



x = df[['Sex','Fare','Age','Parch','SibSp','Pclass']]
y = df['Survived']


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

x = df[['Sex','Fare','Age','Parch','SibSp','Pclass']]
y = df['Survived']

le = LogisticRegression()
tree = DecisionTreeClassifier(criterion='entropy',max_depth=3)
forest = RandomForestClassifier(n_estimators=100)
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)
le.fit(x_train,y_train)
tree.fit(x_train,y_train)
forest.fit(x_train,y_train)

y_pred_le = le.predict(x_test)
y_pred_tree = tree.predict(x_test)
y_pred_forest = forest.predict(x_test)

x = (accuracy_score(y_test,y_pred_le))
y = (accuracy_score(y_test,y_pred_tree))
z = (accuracy_score(y_test,y_pred_forest))
data = {
    "models" : ['logistic_regression','decision_tree','random_forest'],
    "accuracy" : [x,y,z]
}
df_df = pd.DataFrame(data)
#df_df.sort_values(by='accuracy',ascending=False,inplace=True) 
print(df_df)

#'Sex';{0,1},'Fare','Age','Parch','SibSp','pclass
x = [1,15.894,28,1,1,3]
print((le.predict([x])))
print((tree.predict([x])))
print((forest.predict([x])))