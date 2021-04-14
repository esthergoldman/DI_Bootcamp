import random
wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist)
#variables para modificar el juego
posibilities = 5
chances = 0

print("What´s your name?")
name = input()
print("Let´s play a game " + name + " \nGuess a letter " + str(word))
print("You´ve only have " + str(posibilities) + " chances to guess the number")


while chances < posibilities:
  
    print('============================')
    hangman = input("Guess the letter: ")

    if hangman in word_letter:
        letters.append(hangman)
        print(letters, 'Congratulations')
    elif hangman not in word_letter: 
        letters_wrong.append(hangman)
        print(letters_wrong, 'try again')
    if len(letters_wrong) != word:
        print('game over!')