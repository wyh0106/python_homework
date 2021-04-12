import numpy as np
from matplotlib import pyplot as plt 
import math
from math import pi

y = []
x = np.arange(-10, 5, 0.0001)
for i in x:
	y.append(math.cos(2*pi*i) * math.exp(-i) + 0.8)

plt.plot(x, y, color='red', linewidth=3, linestyle='-')
plt.show()
