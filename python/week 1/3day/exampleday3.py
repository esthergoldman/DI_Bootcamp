# Enter a number (as the answer),
# Then ask the user to guess that number,
# They have 3 tries to guess correctly
# At each try, you can tell
# them to guess higher or lower
answer = int(input("Enter your number: "))
for i in range(3):
	guess = int(input("Guess my number: "))
	if guess == answer:
		print("Correct!")
		break
	elif guess > answer:
		print("You guessed too high")
	elif guess < answer:
		print("You guessed too low")
else:
	print("You ran out of guesses!")