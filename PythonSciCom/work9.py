# f(x) = e^x+10x-2
# range:[0,5]
# delta:0.0001

from math import exp

def f(x):
	return exp(x) + 10*x -2

def bis(a=0, b=5, eps=1e-4):
	m = (a+b) / 2

	while abs(f(m)) >= eps:
		if f(m)*f(a) <= 0:
			b = m
		else:
			a = m
		m = (a+b) / 2
	return m

print("x = {:.4f}".format(bis()))