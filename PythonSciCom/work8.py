
for x in range(1,11):
	num = 0
	for y in range(x,0,-1):
		num += 1/y
	print("Harmonic Series:{:6f}".format(num))