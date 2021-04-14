import random
wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist)
word_letter = list(word)
print(' the word has', len(word_letter),'letters')
game = True
letters = [] 
letters_wrong = []

while game:
    print('============================')
    hangman = input("Guess the letter: ")

    if hangman in word_letter:
        letters.append(hangman)
        print(letters, 'Congratulations')
    elif hangman not in word_letter: 
        letters_wrong.append(hangman)
        print(letters_wrong, 'try again')
    if len(letters_wrong) >= 6:
        game = False
        print('game over')
        
    
