#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# Copyright © 2020 ROOM_3033
# All rights reserved.

# filename:$Homework_333$
# description:从名单中生成一份考勤列表，出勤次数为0-10的随机数。

# created by 魏懿航 at 04/09/2020
# QQ:770593981


# ===============RUN_START===============

import os
import random
# 导入文件处理和随机数生成模块


stu_list = {}
student_list = []
temp_dic = {}
# 字典嵌套前的声明


# 从名单中读入学生编号，以及信息
with open('名单.txt', 'r') as Resource_file:
    for line in Resource_file:
        student_list = line.strip().split()
        students_number = student_list.pop(0)
        temp_dic = {'ID': student_list[0], 'Name': student_list[1], 'Class': student_list[2]}
        stu_list[students_number] = temp_dic
        # 用一个字典嵌套来保存每一个学生的编号，姓名，学号和班级
Resource_file.close()
# 关闭文件，避免出现错误


t = '\t'  # 接下来会用到大量制表符，直接用t代替制表符会更简单

# 创建一个txt文件，并且选择覆盖类型的写入方式
res_file = open("考勤列表.txt", 'w')
res_file.write("序号\t          学号\t姓名\t所属自然班级\t出勤总计\t旷课总计\t迟到总计\t请假总计\t事假总计\t公假总计\t早退总计\n")
# 为列表写入表头


# 循环写入所有的出勤信息
for stu_num, stu_info in stu_list.items():
    chuqin = random.randint(0, 10)  # 总出勤次数，由一到十的随机数生成
    kuangke = random.randint(0, 10)  # 旷课次数
    chidao = random.randint(0, 10)  # 迟到次数
    qingjia_zongji = random.randint(0, 10)  # 请假总次数
    qingjia_shi = random.randint(0, qingjia_zongji)  # 公假和事假的次数加起来应当等于请假的总次数
    qingjia_gong = random.randint(0, qingjia_zongji-qingjia_shi)  # 取总次数和事假次数的差为公家次数的随机范围
    zaotui = random.randint(0, 10)  # 早退次数

    # 将学生信息和出勤情况按行写入到文件里
    temp = stu_num + t + stu_info['ID'] + t + stu_info['Name'] + t + stu_info['Class']\
        + t + str(chuqin) + t + str(kuangke) + t + str(chidao) + t + str(qingjia_zongji)\
        + t + str(qingjia_shi) + t + str(qingjia_gong) + t + str(zaotui)
    res_file.write(temp + '\n')

# 关闭文件，避免出现错误
res_file.close()
print("\n======已生成“考勤列表”，请到源代码根目录下查看======")


# ======================RUN_END=========================
