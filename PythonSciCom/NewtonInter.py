import numpy as np
import math

x = np.arange(0, 0.55, 0.05)
y = np.array([0, 37, 71, 104, 134, 161, 185, 207, 225, 239, 250])

def DifTab(X, Y):
	n = len(X)
	A = np.zeros([n,n])

	for i in range(n):
		A[i][0] = Y[i]
	for j in range(1,n):
		for i in range(j,n):
			A[i][j] = (A[i][j-1] - A[i-1][j-1]) / (x[i] - x[i-j])

	Nl = []
	for i in range(n):
		Nl.append(A[i][i])

	return Nl

def NInter(x, X, Y):
	assert len(X) == len(Y)
	n = len(X)

	A = DifTab(X, Y)

	P = 1
	for i in range(n):
		P = A[i] + (x - X[n-1-i]) * P
	return P

F = NInter(0.42, x, y)
print(F)
