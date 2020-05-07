

with open("resource\pi_digits.txt") as pi_file:
    contents = pi_file.read()
    print(contents.rstrip())