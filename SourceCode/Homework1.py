######################################
# 第一次作业:2020.3.29
# 学生:魏懿航
# 学号:2019051107001
# 最后更新于:2020.4.4
######################################
# 程序目标:读入文件Resource.txt并将里面的
#         每一个字统计出现次数，并统计输出
#         出现次数最高的10个字
######################################


# ————————————————————程序初始化——————————————————————
# 将文件读入到station里
file = open(r"resource\Resource.txt", "r")
station = file.read()
# 将整个列表排序，这样会将相同的字符全都相邻，方便后续处理
sta_C = sorted(station)
# 值得注意，在排序后会带来一些奇怪的字符和换行符
sta = []
sequence = {}
# ————————————————————初始化完成——————————————————————


# ——————————————————处理sta_C里存在的非中文字符———————————————————
for temp in sta_C:
    # 通过字符码判断sta_C里的这个字符是否为中文
    if '\u4e00' <= temp <= '\u9fff':
        sta.append(temp)
# 用列表sta写入经过处理的sta_C的元素
# ———————————————————————————处理完成————————————————————————————


# ——————————————————构建字典————————————————————
# 将每个不重复的字提出来，统计出现次数
for A_word in set(sta):
    sequence[A_word] = sta.count(A_word)
# ——————————————————构建完成————————————————————


# ——————————————————输出初始化————————————————————
# 将sequence的键部分单独作为列表value_s取出
value_s = []
for value in sequence.values():  # 由于sequence.values()并不能直接输出列表
    value_s.append(value)  # 所以这里不得不用遍历的方式将它写入一个新列表Value_s
# 将Value_s列表去重并降序排序，得到列表value_p
value_p = []
value_e = set(value_s)  # 和之前一样，set()并不能输出一个列表
for j in value_e:  # 所以这里也需要一个value_p来存储去重后的value_s
    value_p.append(j)
value_p.sort(reverse=True)  # 值得注意的是，去重本身会取消掉排序的效果
# 所以排序放在去重步骤后面
# 按照列表value_p的前10个元素，在sequence的值里找对应的键，并输出
Frequency = []
Rank = {}

for i in range(10):
    Rank[i + 1] = []
    for key, value in sequence.items():
        if value == value_p[i]:  # 如果在sequence中找到value_p中的i项相等的值
            Rank[i+1].append(key)  # 则把它放到对应Rank的i+1键对应的列表里
            Frequency.append(sequence[key])  # Frequency列表用来收集前十名的出现次数

# 将Frequency去重后排序
Frequency = set(Frequency)
Frequency = sorted(Frequency, reverse=True)
# ——————————————————初始化完成————————————————————


# ——————————————————输出部分————————————————————
# 把Rank的键作为名次，值是入选前十的字进行输出
for key, value in Rank.items():
    print("No." + str(key) + ' ', end='')
    for p in value:  # 由于值是一个列表，所以这里需要一个嵌套输出
        if p != value[-1]:  # 避免多输出一个顿号在冒号后面
            print('"' + p + '"', end='、')
        else:
            print('"' + p + '"', end='')
    print(":" + str(Frequency[key-1]) + "次")


# ++++++++++++++++++++++++++++++++++++++++++++++
# ==================程序结束=====================
# ++++++++++++++++++++++++++++++++++++++++++++++
