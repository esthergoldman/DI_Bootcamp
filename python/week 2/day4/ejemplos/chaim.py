# # ex1
# def employee_info(name, salary=9000):

#     print(f"the employee name is {name} and salary is {salary}")


# employee_info("bob", 10000)

# ex2 Create a function called day_of_the_week() that takes one parameter (number from 1-7)

# The function should return the day of the week (sunday, monday ..etc)

# If the number is lower then 1 or bigger then 7 return none.


def day_of_the_week(number):

    if number == 1:
        print("sunday")
    elif number == 2:
        print("monday")
    elif number == 3:
        print("tuesday")
    elif number == 4:
        print("wednesday")
    else:
        print("no idea")


day_of_the_week(1)


# ex3
# Lets simulate a trafic light.

# Write a function that takes a color as a parameter

# Depending on which color was chosen (red, yellow, green) print a response (stop, slow down, go).

# def traffic_light(color):
#     if color == "red":
#         print("stop")
#     elif color == "yellow":
#         print("slow down")
#     elif color == "green":
#         print("go")
#     else:
#         print("whoops")


# traffic_light("red")

# ex4
# create a function that takes a list of nnames as a parameter and prints out a new list with all the names that begin with the letter a

# def names_list(names):
#     a_names = []
#     for name in names:
#         if name[0] == 'a':
#             a_names.append(name)
#     print(a_names)
# names_list(['chaim', 'anna', 'dan', 'aviva'])
# ex5
# Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle.

class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


rec_1 = Rectangle(10, 15)
print(rec_1.area())
