import json
fileN = 'USER.json'

def getN():

    try:
        with open("resource\\" + fileN) as user:
            catch = json.load(user)
            return catch
    except:
        return -1

def New_User():
    with open('resource\\' + fileN,'w') as userN:
            username = input("User: ")
            json.dump(username, userN)
            return username

def C_Hello():

    username = getN()

    if username != -1:
        print('welcome back ' + username)
    else:
        username = New_User()
        print("Info record successful!")
        print("Nice to meet you " + username + '.')

C_Hello()

def D_A_User():
    with open("resource\\" + fileN, 'w'):
        pass

if 'delete' == input():
    D_A_User()