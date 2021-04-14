def older(my_age, friend_age):
    if my_age < friend_age:
       return friend_age
    elif my_age > friend_age:
        return my_age

print(older(20,40))
print(older(60,80))