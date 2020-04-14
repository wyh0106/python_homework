

# def get_name(firstn, lastn, middlen=''):
#     if middlen:
#         full_name = firstn.title() + '·' + middlen.title() + '·' + lastn.title()
#     else:
#         full_name = firstn.title() + '·' + lastn.title()
#     return full_name
#
#
# stu_name = get_name(lastn="bush", middlen="N", firstn="gave")
# print(stu_name)
#
# stu_name = get_name("bull", "shit")
# print(stu_name)

# def define_person(firstn, lastn):
#     person = {'first': firstn, 'last': lastn}
#     return person
#
# stu = define_person('Nicki', 'Masha')
# print(stu)

# def get_name(firstn, lastn):
#     full_name = firstn.title() + '·' + lastn.title()
#     return full_name
#
# while True:
#     print("Input you fucking god damn name! asshole:")
#     fname = input("FN:")
#     if fname == 'q':
#         break
#     Lname = input("LN:")
#     if Lname == 'q':
#         break
#
#     name = get_name(fname, Lname)
#     print("\nOh,I got you got to hell sucking dick name!\nIs " + name + " right?")

# def sayhello(names):
#     for name in names:
#         message = "Hello," + name.title() + ". Welcome！"
#         print(message)
#
# stus = ["pi", "zhu", "kao", "shi"]
# sayhello(stus)

# stus = ["gou", "shi", "pi", "zhu", "bia"]
# signed = []
#
# while stus:
#     current = stus.pop()
#
#     print(current + " is fucking here!")
#     signed.append(current)
#
# print(signed)


# def stu_sign(All_list, sign_list):
#     while All_list:
#         current = All_list.pop()
#         print(current.title() + " is here!")
#         signed.append(current)
#
#
# def show_signed(signed):
#     print("\nThe following students are here.")
#     for stu in signed:
#         print(stu)
#
#
# signed = []
#
# stu_sign(stus, signed)
# show_signed(signed)