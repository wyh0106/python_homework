#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# Copyright © 2020 ROOM_3033
# All rights reserved.

# filename:$Homework_333$
# description:从名单中生成一份考勤列表，出勤次数为0-10的随机数。

# created by 魏懿航 at 04/09/2020
# QQ:770593981
pass

# ===============RUN_START===============

from Load import Load_stu_list as Load
from Header import Header
from Output import Output

# 加载名单文件到一个字典嵌套中
stu_list = Load('名单.txt')

# 生成考勤列表文件，并写入表头
Header()

# 生成随机数并输出
Output(stu_list)


# ======================RUN_END=========================
