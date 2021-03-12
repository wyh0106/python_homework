import matplotlib.pyplot as plt
import numpy as np

x_values = np.arange(2000)
squares = [x**2 for x in x_values]


plt.scatter(x_values, squares,s = 40,c = squares, cmap = plt.cm.jet)

plt.title("Square Numbers", fontsize = 18)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)

plt.tick_params(axis = 'both', labelsize = 14)

plt.show()