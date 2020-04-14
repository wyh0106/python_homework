
# words = "吔屎啦你！\n"
# words += "扑街仔！\n"
#
# while True:
#     duixian = input(words)
#
#     if duixian == '爬':
#         break
#     else:
#         print(duixian + '\n你就只会这一句是吧，傻逼！\n')

# res = 1
#
# while res < 20:
#     if res % 5 == 0:
#         print(str(res))
#     res += 1

# astus = ['wang', 'li', 'zhang', 'hu', 'sun', 'qian', 'ma', 'liu']
# present = []
#
# while astus:
#     catch = astus.pop()
#     print(catch.title() + " is presented.")
#
#     present.append(catch)

response = {}

flag = True

while flag:
    name = input("姓名：")
    q = input("喜欢的食物：")

    response[name] = q

    ask = input("还有吗?\n")

    if ask == 'no':
        flag = False

print("\n结束。\n")

for person, ans in response.items():
    print(person + ':' + ans + '.\n')