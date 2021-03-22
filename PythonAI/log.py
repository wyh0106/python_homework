import json
from sys import exit
fn = "UserData.json"
with open(fn, 'r') as user:
	user = json.load(user)
state = 3

while state:
	name = input("USER NAME: ")					# 输入用户名
	passw = input("PASSWORD: ")					# 输入密码

	sq = 0
	for i in user:
		if name == i['name']:
			if i['state']:						# 判断目标账户是否锁定
				if passw == i['password']:
					print('\n{}, Access granted\n'.format(i['name']))
					exit()
				else:
					state -= 1					# 错误密码计数
					if not state:
						user[sq]['state'] = 0	# 三次错误密码锁定该用户
						with open("UserData.json", "w", encoding='utf-8') as f:
							json.dump(user, f, indent=4)
						print('\nAccount will be locked\n')
						exit()
					print('\nWrong password or account\n')
			else:
				print('\nAccount locked\n')
				exit()
		sq += 1
	print('\n\n')
