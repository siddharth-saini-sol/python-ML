""" encoding numeric labeles"""
from sklearn.preprocessing import LabelEncoder
import pandas as pd 

le = LabelEncoder()
x = [1,2,1,11,2,2,1,3]
le.fit([1,2,3,1,2,1,1])
print(f"classes_ {le.classes_}")
y = le.transform([1,2,1,2])
print(y)
print(le.inverse_transform(y))

"""encoding string  labels"""
str = ['tokyo','paris','london','amstardam','paris','tokyo']
le = LabelEncoder()
print(le.fit(str))
print(le.classes_)
x = (le.transform(str))
print(le.transform(le.classes_))
print(le.inverse_transform(x))

"""using scikitlearn's lebale encoder"""

from sklearn.preprocessing import LabelEncoder
import pandas as pd 

data = pd.DataFrame({
    'Fruit': ['Apple', 'Banana', 'Orange', 'Apple', 'Orange', 'Banana'],
    'Price': [1.2, 0.5, 0.8, 1.3, 0.9, 0.6]
})

data['enc_fruit'] = le.fit_transform(data['Fruit'])
print(data)
print(f"catogorial data{le.classes_}")

"""using pandas catogiral data"""
data['fruit_enc_pan'] = data['Fruit'].astype('category').cat.codes
print(data)
print(dict(enumerate(data['Fruit'].astype('category').cat.codes)))


"""using pandas for ordinal (manula way)"""
data = pd.DataFrame({
    'Satisfaction': ['Low', 'High', 'Medium', 'Low', 'High'],
    'Score': [3, 8, 5, 2, 9]
})
satif = {'Low':0,'Medium':1,'High':2}
data['sat_en']= data['Satisfaction'].map(satif)
print(data)

"""handling unseen data in cat"""
le = LabelEncoder()
train = pd.DataFrame({'City': ['Delhi', 'Mumbai', 'Chennai', 'Delhi']})
#le.classes_
test = pd.DataFrame({'City': ['Mumbai', 'Kolkata']})
train['city_end'] = le.fit_transform(train['City'])
test['city_end'] = test['City'].apply(lambda x : le.transform([x])[0] if x in le.classes_ else -1)
print(train)
print(test)

from sklearn.preprocessing import LabelEncoder 
le = LabelEncoder() 
le.fit([10, 5, 20]) 
print(le.classes_)

"""-------------------------------------------------------------------------------------"""
from sklearn.preprocessing import LabelEncoder

lst = ['cat', 'dog', 'bird', 'cat']
le = LabelEncoder()
le.fit(lst)
le.classes_
print(f"{le.classes_}")
encoded = le.transform(lst)
print(f"encoded{encoded}")
encoded = le.fit_transform(lst)
print(encoded)
inv_enc = le.inverse_transform(encoded)
print(inv_enc)

"""--------------------------------------------------------------------------------------"""
import pandas as pd 
from sklearn.preprocessing import LabelEncoder 

le = LabelEncoder()
data = pd.DataFrame({
    'sr' : [1,2,3,4],
    'City' : ['Delhi', 'Mumbai', 'Chennai', 'Delhi']
})
data['city_enc'] = le.fit_transform(data['City'])
print(data)
print(f"cat data {le.classes_}")
for i in data['City']:
    key = le.transform([i])[0]
    val = le.inverse_transform([key])[0]
    print(key,"->",val)

for city in le.classes_:
    enco = le.transform([city])[0]
    print(city,"-->",enco)

for col_deco in data['city_enc']:
    deco = le.inverse_transform([col_deco])[0]
    print(deco)

"""----------------------------------------------------------------------------------------"""
import pandas as pd
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
data = pd.DataFrame({
    'd' : ['Low', 'Medium', 'High', 'Low']
})
stat = {'Low':0,'Medium':1,'High':2}
data['stat_enc'] = data['d'].map(stat)
print(data)
data['stat_enco'] = data['d'].astype('category').cat.codes
print(data)
"""----------------------------------------------------------------------------------------"""
from sklearn.preprocessing import LabelEncoder
import pandas as pd 

le = LabelEncoder()
train = pd.DataFrame({
    'fruit':['Apple', 'Banana', 'Orange']
})
test = pd.DataFrame({
    'fruit':['Banana', 'Mango']
})
train['fruit_enco'] = le.fit_transform(train['fruit'])
test['fruit_enco'] =  test['fruit'].apply(lambda x: le.transform([x])[0] if x in le.classes_ else -1)
print(train)
print(test)