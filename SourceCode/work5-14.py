

# import json

# fileN = 'data.json'

# with open(fileN) as dataF:
#     number = json.load(dataF)

# print(number)

# import json

# username = input("User:")
# fileN = 'User.json'

# with open(fileN,'a') as user:
#     json.dump(username,user)
#     print('weclome back ' + username + '.')

import json

def USER():
    fileN = 'User.json'

    try:
        with open(fileN) as user:
            username = json.load(user)
            print('welcome back, ' + username + '.')
    except FileNotFoundError:
        with open(fileN,'a') as user:
            username = input("User:")
            json.dump(username,user)
            print('weclome ' + username + '.')

USER()
