
import random2
guess = random2.randint(1, 3)

print("What´s your name?")
name = input()
print("Let´s play a game " + name + " \nGuess a number between 1 to 10? ")
print("You´ve only have 3 chances to guess the number")

num = int(input("Guess the number: "))

if num == guess:
    print("Congratulations! ")
else:
    if num > guess:
        print("Try again! you guessed too high")
    else:
        print("Try again! you guessed too low ")
    
    print("\nYou have 2 more chance")
    num = int(input("Try again: "))
    if num == guess:
        print("Congratulations! ")
    else:
        if num > guess:
            print("Try again! you guessed too high")
        else:
         print("Try again! you guessed too low")

    print("\nYou have 1 more chances")
    num = int(input("last chance: "))
    if num == guess:
        print("Congratulations! ")
    else:
        print("You lose :( ")
   