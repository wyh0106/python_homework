
# function：生成目标文件及表头


def Header():
    # 创建一个txt文件，并且选择覆盖类型的写入方式
    res_file = open("考勤列表.txt", 'w')
    res_file.write("序号\t          学号\t姓名\t所属自然班级\t出勤总计\t旷课总计\t迟到总计\t请假总计\t事假总计\t公假总计\t早退总计\n")
    # 为列表写入表头
    res_file.close()

    print("\n======创建考勤列表成功，表头已生成======")
