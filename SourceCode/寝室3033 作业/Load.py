
# function：加载名单文件，并将信息作为字典嵌套输出


def Load_stu_list(file_name):
    import os
    stu_list = {}
    student_list = []
    temp_dic = {}
    # 字典嵌套前的声明

    # 从名单中读入学生编号，以及信息
    with open(file_name, 'r') as Resource_file:
        for line in Resource_file:
            student_list = line.strip().split()  # 通过空格来分割不同的元素
            students_number = student_list.pop(0)
            temp_dic = {'ID': student_list[0], 'Name': student_list[1], 'Class': student_list[2]}
            stu_list[students_number] = temp_dic
            # 用一个字典嵌套来保存每一个学生的编号，姓名，学号和班级
    Resource_file.close()
    # 关闭文件，避免出现错误

    return stu_list
    # 返回字典嵌套
