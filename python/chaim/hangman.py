import random
wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist)
word_letter = list(word)
print(' the word has', len(word_letter),'letters')
game = True
letters = []
letters_wrong = []

print("Let´s play a game!\nGuess each letter of a word\n")
while game:
    print('============================')
    hangman = input("Guess the letter: ")

    if hangman in word_letter:
        letters.append(hangman)
        print(letters, 'Congratulations')
    elif hangman not in word_letter: 
        letters_wrong.append(hangman)
        print(letters_wrong, 'head')
     
    hangman = (input("Try again: "))
    if hangman in word_letter:
        letters.append(hangman)
        print(letters, 'Congratulations')
    elif hangman not in word_letter:
        letters_wrong.append(hangman)
        print(letters_wrong, 'head, body')

    hangman = input("Guess the letter: ")
    if hangman in word_letter:
        letters.append(hangman)
        print(letters, 'Congratulations')
    elif hangman not in word_letter: 
        letters_wrong.append(hangman)
        print(letters_wrong, 'head,  body, left arm' )

    hangman = input("Guess the letter: ")
    if hangman in word_letter:
        letters.append(hangman)
        print(letters, 'Congratulations')
    elif hangman not in word_letter: 
        letters_wrong.append(hangman)
        print(letters_wrong, 'head,  body, left arm, right arm' )

    hangman = input("Guess the letter: ")
    if hangman in word_letter:
        letters.append(hangman)
        print(letters, 'Congratulations')
    elif hangman not in word_letter: 
        letters_wrong.append(hangman)
        print(letters_wrong, 'head,  body, left arm, right arm, left leg' )
    
    
        game = False
        print('game over')
  



