from scipy.interpolate import lagrange
from matplotlib import pyplot as plt
import numpy as np
import math


x = np.arange(0, 0.55, 0.05)
X = np.arange(0, 0.5, 0.0001)
y = np.array([0, 37, 71, 104, 134, 161, 185, 207, 225, 239, 250])

Y = lagrange(x, y)(X)

plt.plot(X, Y)
plt.scatter(x, y, color = 'red')
plt.show()



