i = 1
sum = 0

while i<=10:
	res = 1
	n = i
	while n>1:
		res = res*n
		n = n - 1

	sum = sum + res
	i = i + 1

print(sum)