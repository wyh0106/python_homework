from collections import Counter

str = input("str:")
str = ' '.join(str)
li = str.split(' ')

res = dict(Counter(li))
res = sorted(res.items(), key=lambda item:item[1] ,reverse=True)
res = dict(res)

for i in res.keys():
	print(i)