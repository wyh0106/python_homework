high = [51, 199, 317, 558, 973, 1231, 1576, 2794, 3369, 4031]
weight = 73*9.8

work = list(map(lambda x:x*weight, high))

for i in work:
	print("work = {:.2f}J".format(i))