
st = []

for nums in range(20):
    new_stu = \
    {
        'sex': 'female',
        'height': '170',
        'age': '17',
        'favourite': 'play basketball',
    }
    st.append(new_stu)

for stu in st[:5]:
        stu['sex'] = 'male'
        stu['height'] = '180'
        stu['favourite'] = 'Games'

for stu in st[3:5]:
        stu['sex'] = 'male'
        stu['height'] = '185'
        stu['favourite'] = 'reading'

for stu in st[:10]:
    print(stu)
