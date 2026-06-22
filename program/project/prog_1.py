import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd 
import numpy as np 

x = [1,2,3,4,5]
y = [2,4,5,4,5]
df = pd.DataFrame(
    {
        'x':[1,2,3,4,5],
        'y':[2,4,5,4,5]
    }
)
mean_x = np.mean(x)
mean_y = np.mean(y)

number = len(x)

num = 0
deno = 0
for i in range(number):
    num += (x[i]-mean_x)*(y[i]-mean_y)
    deno += (x[i]-mean_x)**2

m = num/deno
print(m)
c = mean_y-m*mean_x
print(c)
# ^y = m*-x + c
    
y_pred = []
for i in range(number):
    num = m*x[i]+c
    y_pred.append(num)

SS_em = 0
SS_am = 0
rs = 0
for i in range(number):
    SS_em += (y[i]-y_pred[i])**2
    SS_am += (y[i]-mean_y)**2
    
rs = 1-(SS_em/SS_am)
print(rs)

#plot 
x_max = np.max(x) +1
y_min = np.min(x) -1
x_line = np.linspace(x_max,y_min,100)
y_line = m*x_line+c
plt.plot(x_line,y_line)
plt.scatter(x,y,marker='D')
#plt.plot(x,y,label='without fert best fit line')
plt.show()