
# function：生成并输出出勤情况和学生信息


def Output(stu_list):
    import random
    res_file = open("考勤列表.txt", 'a')

    t = '\t'

    for stu_num, stu_info in stu_list.items():
        chuqin = random.randint(0, 10)  # 总出勤次数，由一到十的随机数生成
        kuangke = random.randint(0, 10)  # 旷课次数
        chidao = random.randint(0, 10)  # 迟到次数
        qingjia_zongji = random.randint(0, 10)  # 请假总次数
        qingjia_shi = random.randint(0, qingjia_zongji)  # 公假和事假的次数加起来应当等于请假的总次数
        qingjia_gong = random.randint(0, qingjia_zongji - qingjia_shi)  # 取总次数和事假次数的差为公家次数的随机范围
        zaotui = random.randint(0, 10)  # 早退次数

        # 将学生信息和出勤情况按行写入到文件里
        temp = stu_num + t + stu_info['ID'] + t + stu_info['Name'] + t + stu_info['Class'] \
               + t + str(chuqin) + t + str(kuangke) + t + str(chidao) + t + str(qingjia_zongji) \
               + t + str(qingjia_shi) + t + str(qingjia_gong) + t + str(zaotui)
        res_file.write(temp + '\n')

    # 关闭文件，避免出现错误
    res_file.close()
    print("\n======已生成“考勤列表”，请到源代码根目录下查看======")