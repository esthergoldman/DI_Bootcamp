# # #exercise 1
# my_fav_numbers = set{1,2,3,4,5}
# my_fav_numbers.add(2,3)
# print(my_fav_numbers)
# my_fav_numbers.remove(5)
# print(my_fav_numbers)

# friends_fav_numbers = set{1,2,3,4,5,6,8}
# our_fav_number = my_fav_numbers + friends_fav_numbers

# #exercise 2
# my_tuple = (5,6,7) #tuples are inmutable, you need to create a new tuple
# my_tupl2 = (5,6,7,8)


# #exercise 3

# for i in range (20, -1, -1)
# 	print(i)


# #exercise 4

# #use Numpy´s arange() fuction to generate the range of floats numbers
# #syntax of numpy´s arange()function arang(start,stop,step)
# import numpy


# for i in numpy.arange(0, 5.5, 0.5):
#     print(i, end=', ')


# #excercise 5
# basket = ["Banana", "Apples", "Oranges", "Blueberries"];
# basket.remove("banana", "Blueberries")
# basket.append("kiwi")
# basket.insert(0,apples)

# len(basket)
# basket=[ ]
# print(basket)

# #exercise 6
# name= "esther"
# while True:
#     try:
#         name = int(input("Please enter your name: "))
#     except ValueError:
#         print("Sorry, try again")
#         continue

#     if name != "esther":
#         print("Sorry, try again")
#         continue
#     else:
#         #name was successfully parsed, and we're happy with its value.
#         #we're ready to exit the loop.
#         break
# if name ==esther:
#     print("ok")
# else:
#     print("try again")


# #exercise 7

# #loop
# #list1 = [1,2,3,4,5,6,7,8,9,10]
# #for num in list1:
# #	if num % 2 == 0:
# #		print(num, end = " ")

# #while loop
# list1 = [2,4,5,6,8,9,22,34,61,1]  #list of numbers
# num = 0

# while(num < len(list1))
# 	if num % 2 == 0;  #checking condition
# 		print(list1[num],end = " ")
# 		num += 1 #increment num


# #exercise 8

# multiples_3= [ ]
# for i in range (3,30): #bucle del 3 al 30
# 	if multiple(i,3):
# 		multiples_3.append(i)
# print(multiples_3)


# #exercise 9

# multiples_5= []

# for i in range (1500,2700):
# 	if multiple(i,5):
# 		multiples_5.append(i)


# print(multiples_5)


# divisible = 7
# min = 1500
# max = 2700

# num =min
# while num <= 2700:
# 	if (num % divisible == 0):
# 		print(format(num))


# exercise 10

# list_fruits = input("Enter your favorite fruits:\n ").split(" ") 
# fruit = input("Enter a fruit: ")
# if fruit in list_fruits:
#     print("You chose one of your favorite fruits! Enjoy!") 
# else:
#     print("You chose a new fruit. I hope you enjoy it too!")



#ex11

# active = True
# toppings = []
# while active: 
#     user = input("Please enter enter a series of pizza toppings.\nEnter 'quit' when you are finished:\n ")
#     if user == 'quit':
#         total = 10 + (2.5*len(toppings))
#         print(f'your´re toppings are {toppings}  and your total is {total}')
#         break
#     else:
#         print(f"i'll add {user} to you're pizza")
#         toppings.append(user)

#ex12 
# active = True
# total = 0
# while active:
#     person = int(input("whats your age?\nEnter 000 when you are finished:\n "))

#     if person == 000:
#         break
#     elif person <= 3 and person >= 1:
#         pass
#         print('free')       
#     elif person >=3 and person <= 12:
#         total  += 10
#     else:
#         total += 15
# print(f'total is {total}')



# active = True
# yes = []

# while active:
#     age = int(input("what´s your age?\nEnter 000 when you are finished\n"))

#     if age >= 1 and age <= 15:
#         print('you cant watch the movie')
#     elif age >= 16 and age <= 21:
#         print('you can´t watch the movie')
#     elif age >= 22:
#         print('yes, you can watch themovie,the ticket is $15')
#         yes.append(age)
#     elif age == 000:
#         break
# print(yes)
 

