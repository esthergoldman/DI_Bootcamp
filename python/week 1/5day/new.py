#1 create list of people, name by one input
#2 create loop through list of people and add all names that begin with letter A to a new list and print

list1 = input("add your name, when you are finish put exit\n")
names = []

while list1 != "exit":
    if list1[0] == "a":
        names.append(list1)
    list1 = input("add your name, when you are finish put exit\n")

print(names)
