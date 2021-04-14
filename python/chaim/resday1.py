# name = 'chaim'
# name2 = 'ben'
# print('hello {} and {}'.format(name, name2))
# print(f'hello {name} and {name2}')
# if color.islower() == 'red':
# if color.isupper() == 'RED':
# name_list = ['b', 'e', 'n']
# print(''.join(name_list))
# date = '2021-10-25'
# print(date.split('-'))
# age = int(input('whats your age?\n'))
# if age > 10 and age < 20:
#     print('between 10 and 20')
# elif age > 20:
#     print('to old')
# else:
#     print('to young')
# month = int(input('input a month (1 to 12).'))
# if month >= 3 and month <= 5:
#     print('spring')
# elif month >= 6 and month <= 8:
#     print('summer')
# elif month >= 9 and month <= 11:
#     print('autumn')
# elif month == 0 or month > 12:
#     print('incorrect month!')
# elif month >= 12 or month <= 2:
#     print('winter')
# names = ['chaim', 'dov', 'esther']
# names.append('aviva')
# names.insert(2, 'josh')
# print(names)
# fruits = ['apples', 'bananas', 'oranges']
# fruits.remove('bananas')
# print(fruits)
# numbers = [1, 2, 5, 7, 4, 6, 7, 3, 5, 6, 8, 5, 68, 2, 3, 5]
# nums = set()
# for num in numbers:
#     nums.add(num)
# print(nums)
# name = 'chaim'
# print(list(name))
# phonebook = {
#     'person1': {'name': {'f_name': 'chaim', 'l_name': 'wiesner'}, 'phone': 898975975},
#     'person2': {'name': {'f_name': 'aviva', 'l_name': 'boo'}, 'phone': 84444975},
#     'person3': {'name': {'f_name': 'esther', 'l_name': 'foo'}, 'phone': 11111175},
#     'person4': {'name': {'f_name': 'dov', 'l_name': 'moo'}, 'phone': 889898975},
# }
# phonebook['person5'] = {
#     'name': {'f_name': 'josh', 'l_name': 'blah'}, 'phone': 875}
# phonebook['person6'] = {
#     'name': {'f_name': 'mary ann', 'l_name': 'duetel'}, 'phone': 9998975}
# phonebook2 = {
#     'person7': {'name': {'f_name': 'jon', 'l_name': 'doe'}, 'phone': 88}
# }
# phonebook.pop('person3')
# phonebook.update(phonebook2)
# pp.pprint(phonebook)
# for with range
# for loop with in
# while counter
# while loop flag
# for i in range(20, 51, 2):
#     print(i)
# counter = 0
# while counter <= 50:
#     print(counter)
#     counter += 1
# counter = 50
# while counter <= 250:
#     if counter % 3 == 0:
#         print(counter)
#     counter += 1
# active = True
# name_list = []
# while active:
#     name = input('input you name when finished input exit\n')
#     if name != 'exit':
#         name_list.append(name)
#     else:
#         active = False
# print(name_list)
16:03
# import random
# wordslist = ['correction', 'childish', 'beach', 'python', 'assertive',
#              'interference', 'complete', 'share', 'credit card', 'rush', 'south']
# word = random.choice(wordslist)
# active = True
# lifes = 5
# letter_list = list(word)
# star_list = []
# for i in range(len(letter_list)):
#     star_list.append('*')
# wrong = 0
# loop = 0
# used = []
# while active:
#     if word == ''.join(star_list):
#         active = False
#         print('Winner!!')
#     elif word != ''.join(star_list) and lifes > 0:
#         letter = input(f'Please input a letter you have {lifes} lifes left')
#         used.append(letter)
#         for let in letter_list:
#             if let == letter:
#                 star_list[loop] = let
#             else:
#                 wrong += 1
#             loop += 1
#         if wrong == len(letter_list):
#             lifes -= 1
#         else:
#             print(''.join(star_list))
#         wrong = 0
#         loop = 0
#         print(used)
#     elif lifes == 0:
#         active = False
#         print('You lose')s