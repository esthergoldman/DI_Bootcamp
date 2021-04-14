# Exercise 2 : Cinemax #2
# “Continuation of Exercise Cinemax of Week4Day2 XP”

# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free
# if they are between 3 and 12, the ticket is $10;
# and if they are over age 12, the ticket is $15 .
# Here is the object you will work with : family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# Using a for loop, the dictionary above, and the instructions, print out how much each family member will need to pay alongside their name
# After the loop print out the family’s total cost for the movies
# Bonus: let the user input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty)


family_dict = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total_price= 0

for person in family_dict:
    # print(family_dict[person])
    if family_dict[person] < 4:
        print('You are too young')
        continue
    elif family_dict[person] >= 4 and family_dict[person] < 12:
        total_price += 10
    else:
        total_price += 15
print(total_price)






# # age = int(inpt["what is your age: "])

# # if age < 4:
# #     print("the ticket priceis free")
# # elif age >= 3 and age < 12:
# #     print("the ticket is $15")
# #     #print(age)

# family_list = []

# name_age = input("please input your name, your age. Put a comma inbetween name/age: then write exit:")
# while name_age != "exit":
#     person_info = name_age.split(",")
#     family_list.append(person_info)
#     name_age = input("please input your name, your age. Put a comma inbetween name/age: then write exit:")
# #print(family_list)

# total_price = 0
# for person_info in family_list:
#     if int (person_info[1]) < 4:
#         print("You are too young")
#         continue 
#     elif (person_info[1]) >= 4 and int(person_info[1]) < 12:
#         total_price += 10
#     else:
#         person_info +=15
# print(total_price)


# permitted= []

# for person_info in family_list:
#     if person_info[1] >= 16 and person_info <=21:
#         print(f"{peson_info[0]}you can watch the movie")
#         permitted.append(person_info[0])
#     else:
#         print("you are too your or old")
# print(permitted) 







# if age < 4:
#     print("the ticket priceis free")
# elif age >= 3 and age < 12:
#     print("the ticket is $15")
# else:
#     print("the tickes is $15")
#     #print(age)


