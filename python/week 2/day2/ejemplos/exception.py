animals = ["dog", "cat"]
user_input = input("Which animal (number) do you want? ")
try:
	index = int(user_input)
	print(animals[index])
except ValueError:
	print("Your input must be a number")
except IndexError:
	print(f"Number must be between 0 and {len(animals)}")
except Exception:
	pass #catch all other exceptions
finally:
	print("We are done.")