import numpy as np

x = np.arange(0, 0.55, 0.05)
y = np.array([0, 37, 71, 104, 134, 161, 185, 207, 225, 239, 250])

def lagrange(x, X, Y):
	assert len(X) == len(Y)
	n = len(X)
	Pn = 0

	for i in range(n):
		bi = 1
		for j in range(n):
			if j != i:
				bi *= (x-X[j])/(X[i]- X[j])
		Pn += Y[i] * bi
	return Pn

F = lagrange(0.42, x, y)
print(F)
