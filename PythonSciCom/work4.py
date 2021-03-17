
power = int(input("power: "))

if power<0:
	print("Invalid Value!")
else:
	if power<=50:
		print("cost = {:.2f}".format(power*0.53))
	else:
		print("cost = {:.2f}".format((power-50)*0.58 + 26.5))