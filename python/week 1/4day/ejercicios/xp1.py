#ex1
# def display_message():
#     print("im learning functions")
# display_message()
   

#ex2

# def favorite_book(title):
#     print(f"One of my favorite books is {title} ")


# favorite_book("alice in wonderland")

#ex3
# def describe_city(city, country="china"):
    
#     print(city +" is in "+ country)
#     #print(f"{} is in {}")

# describe_city("paris","france")
# describe_city("berlin","germany")
# describe_city("roma")

#ex4
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


#ex6

# def show_magicians(magicians):
#     for magician in magicians:
#         print(magician)


# name_magicians = ["cooperfield", "houdini", "burton", "robbins" ]
# show_magicians(name_magicians)

# def make_great(name_magicians):
#     for name_magicians in name_magicians:
#         print("the Great",name_magicians)
# make_great(name_magicians)

#ex7.1

from datetime import date

def get_age(age):
    today = date.today()
    return today.year - age.year - ((today.month, today.day) < (age.month, age.day))

print(get_age(date(1991,1,29)))
print(get_age(date(1989,1,12)))

#def can_retire(gender,date_of_birthday):
