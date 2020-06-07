import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()

para = Axes3D(fig)

# u = np.linspace(0,13,1000)
# x = np.sin(u)
# y = np.cos(u)
x = np.arange(-5, 5.1, 0.1)
y = np.arange(-5, 5.1, 0.1)

X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2

from matplotlib import cm

para.plot_surface(X, Y, Z, alpha=0.75, cmap='coolwarm')

para.contourf(X, Y, Z, zdir = 'z', offset = -10, cmap = plt.get_cmap('coolwarm'))
para.contourf(X, Y, Z, zdir = 'y', offset = 7, cmap = plt.get_cmap('rainbow'))
para.contourf(X, Y, Z, zdir = 'x', offset = -7, cmap = plt.get_cmap('rainbow'))

para.set_ylabel('Y')
para.set_ylim(-5, 7)
para.set_xlabel('X')
para.set_xlim(-7, 5)
para.set_zlabel('Z')
para.set_zlim(-10, 50)

plt.show()
