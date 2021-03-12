
#students = {'li':'2019001','wang':'2019002','sun':'2019003','ma':'2019004'}

#print(students['wang'])
#students['chen'] = '2019005'

#print("sun's ID is " + students['sun'])

#for key in students.keys():
#    print(key + '\n')

languages = {
    'li':'java',
    'wang':'c',
    'song':'swift',
    'ma':'python'
    }
for name in sorted(languages.values()):
    print(name + '\n')
for pick in set(languages.values()):
    if pick =='wang':
        print(pick)
    elif pick == 'song':
        print(pick)