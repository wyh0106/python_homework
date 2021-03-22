import string

s = input("string:\n")

letter = space = digit = others = 0

for c in s:
	if c.isalpha():
		letter += 1
	elif c.isspace():
		space += 1
	elif c.isdigit():
		digit += 1
	else:
		others += 1

print("char = {}\ndigit = {}\nothers = {}\nspace = {}".format(letter, space, others, digit))