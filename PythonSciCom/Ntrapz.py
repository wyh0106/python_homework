from math import sqrt
import numpy as np

def Ntrapz(x, y):
	assert len(x)==len(y)
	N = len(x) - 1
	I = 0
	for i in range(N):
		I += 0.5*(x[i+1] - x[i])*(y[i+1] + y[i])

	return I

m = 0.75
x = np.arange(0, 0.55, 0.05)
y = np.array([0, 37, 71, 104, 134, 161, 185, 207, 225, 239, 250])
Fx = Ntrapz(x, y)
print(Fx)
print(sqrt(2*Fx/m))