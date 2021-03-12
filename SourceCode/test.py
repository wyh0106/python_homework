from random import random
from math import exp,sqrt,pi


def normal_distribution(x, mu, sigma):
	a= 1/sqrt(x*pi)*sigma
	b=-(x-mu)**2/(x*sigma**2)
	c=a*exp(b)
	return c


a1 = random.random()*10
a2 = random.random()
a3 = normal_distribution(a1,a1,a2)

print(a1,a2,a3)