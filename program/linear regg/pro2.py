import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd 
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([3, 5, 6, 9, 10, 12, 13, 16, 17, 19])
x_mean = np.mean(x)
y_mean = np.mean(y)
m = np.sum((x-x_mean)*(y-y_mean)) / np.sum((x-x_mean)**2)
c = y_mean - (m * x_mean)
print(f"m:{m}")
print(f"c:{c}")
Y_pred_arr = []
for i in x:
    val = m*i +c
    Y_pred_arr.append(val)
total = 0
for i in Y_pred_arr:
    total = total+i
mse = np.mean((Y_pred_arr - y)**2)
print("value of mse", mse)
alpha = 0.1
beta0 = 0 
beta1 = 0
r = 1000
n = len(x)
for i in range(r):
    y_p = beta0 + beta1*x
    error = y_p - y
    gradient0 = 2/n*np.sum(error)
    gradient1 = 2/n*np.sum(error*x)
    beta0 = beta0 - alpha*gradient0
    beta1 = beta1 - alpha*gradient1

x_ip = int(input("enter independent"))
Y_pred_ = beta0 + beta1*x_ip
Y_pred = beta0 +beta1*x

print(f"prediction : {Y_pred_}")

plt.plot(x,Y_pred)
plt.scatter(x,y)
plt.show()