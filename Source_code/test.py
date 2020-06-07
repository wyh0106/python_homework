import numpy as np
import matplotlib.pyplot as plt

x = [5.335, 4.653, 0.632, 5.328, 3.226, 6.661, -3.331, 3.341, 1.975, -2.095, 4.003, 2.008]

a = [5.33, 4.67, 0.67, 5.33, 3.33, 6.67, -3.33, 3.33, 2, -2, 4, 2]

d = []
count = 0

for X in x:
	d.append((X-a[count])/a[count]*100)
	count += 1

print(d)

