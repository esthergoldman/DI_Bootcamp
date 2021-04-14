# create a function that takes a list of
#  numbers as a parameter and prints the sum 
#  of the all the numbers in the list

# def sum_list(nums):
#     sum = 0
#     for num in nums:
#         sum += num
#     return total
# print(sum((2,2)))



# ex4
# import random 
# def number(num1):
#    num2= random.randint(1,100)

#    if num1 == num2:
#        print("ok")
#    else:
#        print("buh")
        
# number(60)

#ex5
# def make_shirt( size="large",text="i love python"):
#     print(f"your size is:  {size}  and your message is: {text}")

# make_shirt(39,"my name") #positional argument
# make_shirt(size="38", text="your name") #keyword argument
# make_shirt()
# make_shirt(size="medium")
# make_shirt("small","hello world")


# ex6

# def show_magicians(magicians):
#     for magician in magicians:
#         print(magician)


# name_magicians = ["cooperfield", "houdini", "burton", "robbins" ]
# show_magicians(name_magicians)

# def make_great(name_magicians):
#     for name_magicians in name_magicians:
#         print("the Great",name_magicians)
# make_great(name_magicians)


# create a a function called shopping list 
# that asks the user for items untill 
# the user decides to exit then prints out the list


def shopping_list():
    items = []
    active = True
    while active:
        user = input("Please enter your items: and then exit ") 
        if user != 'exit':
            items.append(user)
        else:
            active = False
    print(items)  
        
shopping_list()