import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,4,5,4,5]
data = pd.DataFrame({
    "x": [1,2,3,4,5] ,
    "y":[2,4,5,4,5]
})

print(data)

x_mean = np.mean(x)
y_mean = np.mean(y)
print(x_mean, y_mean)


sum_x = 0
sum_yx = 0
for i in range(len(x)):
    sum_x += (x[i] - x_mean)**2
    sum_yx += (y[i] - y_mean)*(x[i]-x_mean)
print(sum_x)
print(sum_yx)

m_slop = (sum_yx)/(sum_x)
c = y_mean - (m_slop*x_mean)
print(c)
y_pred = []
for i in range(len(x)):
    y_pr = m_slop*x[i] + c
    y_pred.append(y_pr)
print(y_pred)

ss_tot = 0 
ss_res = 0
for i in range(len(y)):
    ss_tot += (y[i]- y_mean)**2
    ss_res += (y[i] - y_pred[i])**2
print(ss_res)
print(ss_tot)

r2 = 1- (ss_res/ss_tot)
print(r2)

X = np.linspace(1,5,100)
Y = m_slop* X + c

plt.plot(X,Y,)
plt.scatter(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()