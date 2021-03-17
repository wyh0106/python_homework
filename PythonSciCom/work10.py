# f(x) = cos(2*pi*x)*exp(-x) + 1.2
# range: 0.7, 4

from math import exp
from math import cos
from math import pi

def f(x):
	return cos(2*pi*x)*exp(-x) + 1.2

def trapz(a=0.7, b=4, N=100):
	h = (b-a) / N
	I = 0

	for i in range(N):
		x1 = a + i*h
		x2 = a + (i+1) * h
		S = 0.5*h*(f(x1) + f(x2))
		I += S
	return I

print("result = {:.6f}".format(trapz()))