
def isOdd(num):
	if not((num*10)%10):
		if num%2:
			return True
		else:
			return False
	else:
		print("It is not int number!")

num = eval(input("num:"))

print(isOdd(num))