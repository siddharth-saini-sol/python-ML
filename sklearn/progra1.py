from sklearn.datasets import load_iris 

iris = load_iris()

X = iris.data
y = iris.target

feature_name = iris.feature_names
target_name = iris.target_names

print(f'target name is {target_name}')
print(f'feature name is {feature_name}')
print(type(X))
print(X[:5])

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.4,random_state=1)

print(f"x train set {X_train.shape}")
print(f"X test {X_test.shape}")
print(f"y train {y_train.shape}")
print(f"y test{y_test.shape}")



from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()

lst = ['bird','angey','bird','animal','mamal','animal']

encoded = encoder.fit_transform(lst)

print(encoded)