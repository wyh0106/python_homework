import numpy as np
from matplotlib import pyplot as plt

def newton_interpolation(x,X,Y):
    """
    计算x点的插值
    """
    sum=Y[0]
    temp=np.zeros((len(X),len(X)))
    #将第一行赋值
    for i in range(0,len(X)):
        temp[i,0]=Y[i]
    temp_sum=1.0
    for i in range(1,len(X)):
        #x的多项式
        temp_sum=temp_sum*(x-X[i-1])
        #计算均差
        for j in range(i,len(X)):
            temp[j,i]=(temp[j,i-1]-temp[j-1,i-1])/(X[j]-X[j-i])
        sum+=temp_sum*temp[i,i] 
    return sum

x = np.arange(0, 0.55, 0.05)
y = np.array([0, 37, 71, 104, 134, 161, 185, 207, 225, 239, 250])

F = newton_interpolation(0.42, x, y)

plt.plot(x, y)
plt.scatter(x, y, color = 'red')
plt.scatter(0.42, F, color = 'blue')
plt.show()