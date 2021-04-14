import random
wordslist = ['correction', 'childish', 'beach', 'python', 'assertive',
             'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist)
active = True
lifes = 5
letter_list = list(word)
star_list = []
for i in range(len(letter_list)):
    star_list.append('*')
wrong = 0
loop = 0
used = []
while active:
    if word == ''.join(star_list):
        active = False
        print('Winner!!')
    elif word != ''.join(star_list) and lifes > 0:
        letter = input(f'Please input a letter you have {lifes} lifes left')
        used.append(letter)
        for let in letter_list:
            if let == letter:
                star_list[loop] = let
            else:
                wrong += 1
            loop += 1
        if wrong == len(letter_list):
            lifes -= 1
        else:
            print(''.join(star_list))
        wrong = 0
        loop = 0
        print(used)
    elif lifes == 0:
        active = False
        print('You lose')