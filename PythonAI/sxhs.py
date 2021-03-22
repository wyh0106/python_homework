

for i in range(100, 1001):
	Huns = int(i/100)
	Tens = int((i-Huns*100) / 10)
	Ones = int(i-Huns*100-Tens*10)

	if i==Huns**3 + Tens**3 + Ones**3:
		print(i)