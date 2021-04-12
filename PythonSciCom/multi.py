def multi(*mul):
	total = 1

	for n in mul:
		total *= n
	return total

print(multi(1,2,3,4,5))