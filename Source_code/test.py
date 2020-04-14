sum = 0
num = 16
while(num <= 100):
    print(str(num) + '的三次方:' + str(pow(num, 3)))
    sum = sum + pow(num, 3)
    num += 2

print('\n以上总和为' + str(sum))
