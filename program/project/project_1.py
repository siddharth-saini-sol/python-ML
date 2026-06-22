import pandas as pd
import numpy as np 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Hours_Studied': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                      11, 12, 13, 14, 15, 16, 17, 18, 19, 20],

    'Exam_Score': [42, 45, 50, 54, 57, 61, 64, 69, 72, 76,
                   79, 84, 87, 91, 94, 98, 101, 106, 109, 113]
})

print(df)
reg = LinearRegression()
x = df[['Hours_Studied']]
y = df['Exam_Score']
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=10)
reg = reg.fit(x_train,y_train)
y_pred = reg.predict(x_test)
r2 = r2_score(y_test,y_pred)
print(r2)
plt.scatter(x,y,label='actual')
plt.plot(x_test,y_pred,label='predicted')
#plt.legend()
#plt.show()
print(reg.predict([[12]]))
print(reg.predict([[1]]))
print(reg.predict([[2400]]))