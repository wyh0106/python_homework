

# def G(wei, *something):
#     for i in something:
#         print('You ordered ' + str(wei*500) + "g Noddles will add " + i, end=' ')
#
#
# G(2, 'shit', 'pance')

def intro_stu(first, last, **stu_info):
    info = {}
    info['first'] = first
    info['last'] = last

    for key, value in stu_info.items():
        info[key] = value

    return info


stu1 = intro_stu('zhang', 'gou', location='nanji', age=18)
print(stu1)
