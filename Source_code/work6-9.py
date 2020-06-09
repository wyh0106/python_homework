import matplotlib.pyplot as plt
from random_work import RandomWalk

RandomWalk = RandomWalk()

RandomWalk.fill_walk()

x = RandomWalk.x_values
y = RandomWalk.y_values

plt.scatter(x[0], y[0], c = 'blue')
plt.scatter(x, y, s = 0.5, c = 'red')
plt.scatter(x[-1], y[-1], c = 'blue')

plt.show()

