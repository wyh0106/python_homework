from random import randint

def birth():
	birthday = []
	for _ in range(23):
		birthday.append(randint(1,366))

	set1 = set(birthday)
	if len(birthday)!=len(set1):
		return 1
	else:
		return 0

sum = 0
for _ in range(10**5):
	sum += birth()

print("{:.2f}%".format(sum/10**3))