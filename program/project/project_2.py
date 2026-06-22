import pandas as pd
import numpy as np 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
df = pd.DataFrame({
    'Area': [3000,4000,5000,6000,7000,7000,8000,9000,10000,11000,12000,12200],
    
    'Bedrooms': [1,2,1,2,3,4,1,2,3,4,6,7],
    
    'Society': [
        'Normal',
        'Normal',
        'Normal',
        'Elite',
        'Normal',
        'Elite',
        'Normal',
        'Elite',
        'Normal',
        'Elite',
        'Elite',
        'Elite'
    ],
    
    'House_Price': [
        28,
        42,
        48,
        75,
        68,
        90,
        78,
        110,
        95,
        135,
        170,
        190
    ]
})

soc = {
    'Normal':'rajendra nagar',
    'Elite': 'vijay nagar'
}
df['Society'] = df['Society'].map(soc).fillna(False)
df['Society'] = df['Society'].str.replace(" ","_").str.lower().str.strip()
print(df)
encoder = LabelEncoder()
encoded = encoder.fit_transform(df['Society'])
df['Society_en'] = encoder.fit_transform(df['Society'])

x = df[['Area','Bedrooms','Society_en']]
y = df['House_Price']

reg = LinearRegression()
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_state=42)
#x_train.corr()
reg = reg.fit(x_train,y_train)
y_pred = reg.predict(x_test)
#print(y_pred)
r2 = r2_score(y_test, y_pred)
print(r2)
print(reg.predict([[4500,3,1]]))
print(reg.predict([[4500,3,0]]))