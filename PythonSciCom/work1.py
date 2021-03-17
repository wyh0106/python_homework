def fuc(x):
	if x>0 and x<=3:
		return 10
	elif x>3 and x<=10:
		return(10+(x-3)*1.4)
	elif x>10:
		return(19.8+(x-10)*2.1)

s1 = 2
s2 = 5
s3 = 15

print(fuc(s1), fuc(s2), fuc(s3))