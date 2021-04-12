from random import randint

num = randint(0,9)
guess = int(input("Guess a number from 0~9:"))
count = 1

while guess!=num:
	if guess>num:
		print("Too big")
	elif guess<num:
		print("Too small")
	guess = int(input("Guess a number from 0~9:"))
	count += 1

print("Yes you are right!")
print("you have guessed {} times".format(count))