

# sum = 0
# n = '0'

# for i in range(1,7):
#     n += str(6)
#     sum += int(n)

# print('\n' + str(sum))

class bug():

    def __init__(self, kind, several):
        self.kind = kind
        self.several = several

    def warning(self):
        print(self.kind.title() + "Have a warning in your code!")

    def error(self):
        print(self.kind.title() + "Have a Error in your code")


new_bug = bug('caps is unlock!', 3)
print("bug kind is:" + new_bug.kind.title() + '.')
print("Have " + str(new_bug.several) + ' bug.')
