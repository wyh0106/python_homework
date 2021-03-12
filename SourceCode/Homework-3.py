#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# description：冒泡排序,可选择排序方式
# created by 魏懿航 at 04/09/2020
pass

# ==========RUN_START==========
# 输入一个数字列表
number = list(map(int, input("请输入需要排序的数字（用空格隔开）:\n").split()))
kind = input("\n降序（Descend）或升序（Ascend）？\n（输入D/A）:")

count1 = 0  # 初始化外层循环的计数

if kind == 'D' or kind == 'd':
    # 遍历列表的第一项到倒数第二项
    while count1 <= (len(number)-2):  # 列表从0起始，故倒数第二项为元素数-2
        count2 = count1 + 1  # 初始化内层循环的计数
        # 遍历列表的count1 + 1项至最后一项
        while count2 <= (len(number)-1):  # 同理，最后一项为元素数-1
            # 判断每两项是否前项小于后项，如果是，则调换位置，把大的数放到前面
            if number[count1] < number[count2]:
                mid = number[count2]
                number[count2] = number[count1]
                number[count1] = mid

            count2 += 1  # 内层循环计数累加
        count1 += 1  # 外层循环计数累加
    # 输出
    print("\n\n=====排序完成=====\n")
    for i in number:
        print(str(i), end=' ')

elif kind == 'A' or kind == 'a':
    # 遍历列表的第一项到倒数第二项
    while count1 <= (len(number) - 2):  # 列表从0起始，故倒数第二项为元素数-2
        count2 = count1 + 1  # 初始化内层循环的计数
        # 遍历列表的count1 + 1项至最后一项
        while count2 <= (len(number) - 1):  # 同理，最后一项为元素数-1
            # 判断每两项是否前项小于后项，如果是，则调换位置，把大的数放到前面
            if number[count1] > number[count2]:
                mid = number[count2]
                number[count2] = number[count1]
                number[count1] = mid

            count2 += 1  # 内层循环计数累加
        count1 += 1  # 外层循环计数累加
    # 输出
    print("\n==========排序完成==========\n")
    for i in number:
        print(str(i), end=' ')

else:
    print("\nWarning!\n请输入正确的排序方式")
    # 错误提示

# ==========RUN_END==========
