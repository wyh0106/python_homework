def LeapYear(year):
	if year%4 == 0:
		return True
	else :
		return False

def DaysNum(date):
	mon = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 提取年月日   20200305
	year = int(date[:4])
	month = int(date[4:6])
	day = int(date[6:])
# 闰年二月多一天
	if LeapYear(year):
		mon[1] = 29
# 统计前面月份的天数
	temp = 0
	for i in mon[:month-1]:
		temp += i
	return temp+day

print(DaysNum(input()))