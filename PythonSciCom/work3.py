
tax = int(input("Income(yuan): "))

if tax < 0:
	print("NULL")
else:
	if tax<=5000:
		print(0)
	elif tax<8000:
		print(tax*0.03)
	elif tax<=17000:
		print(tax*0.1)
	elif tax<=30000:
		print(tax*0.2)
	elif tax<=40000:
		print(tax*0.25)
	elif tax<=60000:
		print(tax*0.30)
	elif tax<=85000:
		print(tax*0.35)
	else:
		print(tax*0.45)