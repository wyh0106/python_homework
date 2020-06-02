import numpy as np

A = np.array([3., 3., 3., 3.])
X = np.array([3.012, 2.918, 3.004, 3.014])

E = X - A
delta = E/A*100

print(np.around(delta, 2))
