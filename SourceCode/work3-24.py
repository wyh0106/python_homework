stus = {
    'stu1': {
        'first_name': 'yanzen'
    },
    'stu2': {
        'first_name': 'kk'
    },
    'stu3': {
        'first_name': 'wine'
    }
}

for num,information in stus.items():
    print("name:" + num + '\n')
    print("\t" + information['first_name'])
message = input("Give me some massage:")
message += "."
print("You just say :" + message +"\nright?")

words = "Worldline Zero"
words += " is a best sword\n"

message = ''

while message != "worldline zero is a best sword":
    message = input("enter something\n")
    if message != "worldline zero is a best sword":
        print(message)
    else:
        print('yes!')
