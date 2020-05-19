
# filename = 'resource\\test_massage.txt'

# with open(filename,'w') as fc:
#     fc.write("today is a nice day.\n")
#     fc.write('sky is clear, and air is frash!')

# print("input two number,calculator will divison them")
# print("press 'p' to break the loop")

# while True:
#     fn = input("\ninput the numerator:")
#     if fn == 'q':
#         break
#     sn = input("\ninput the denominator:")
#     if sn == 'q':
#         break
#     try:
#         result = int(fn)/int(sn)
#     except ZeroDivisionError:
#         print("can't division zero!")
#     else:
#         print("result is %d" %result)

filename = 'resource\\alice.txt'

try:
    with open(filename) as alice:
        contents = alice.read()
except FileNotFoundError:
    print("File is not found")
else:
    words = contents.split()
    number = len(words)
    print(number)