def LeapYear(year):
	if year%4 == 0:
		return True
	else :
		return False

print(LeapYear(int(input())))