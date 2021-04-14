# Exercise 1 : Hello World-I Love Python
# print("hello world\n" * 4 + "i love python\n" * 4)


# Exercise 2 : What Is The Season ?


season = int(input("input a month (1 to 12)\n "))


if season >= 3 and  season <= 5:
    print("spring")
elif season >= 6 and season <= 8:
    print("summer")
elif season >= 9 and season <= 11:
    print("autumn")
elif season <= 12 and season >= 1:
    print("winter")
else:
    print("plese months between 1 to 12")
