str = input("string:")

chi = 0
eng = 0
num = 0
spa = 0
oth = 0

for ch in str:
	if '\u4e00' <= ch <= '\u9fff':
		chi += 1
	elif 'A' <= ch <= 'z':
		eng += 1
	elif '0' <= ch <= '9':
		num += 1
	elif ch == ' ':
		spa += 1
	else:
		oth += 1

print("Chinese:{}\nEnglish:{}\nNumber:{}\nSpace:{}\nOther:{}".format(chi, eng, num, spa, oth))

