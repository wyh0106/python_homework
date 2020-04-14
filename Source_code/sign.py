

# UserName = input("\nUser:")
# Password = input("Password:")

# if(UserName == "admin" and Password == "tesla"):
#     print("\n=====Login successful=====")
# else:
#     print("Username or password is incorrect")

k = 1
for i in range(2,100):
    if(i%3 == 0):
        print("%d-%d"%(k, i))
        k = k - i
    if(i%3 != 0):
        print("%d+%d"%(k, i))
        k = k + i

print("\n%d"%(k))