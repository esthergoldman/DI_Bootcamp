# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def age(self)
#         if age >= 10:
            
    
#     def display(self)
#         print(f' the oldest cast is {self.cat}')

# cat1 = Cat('kitty', 7)
# cat2 = Cat('molly', 8)
# cat3 = Cat('bob', 10)


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def oldest (self, other, other2):
        oldest = 0
        if self.age > other.age and self.age > other2.age:
            oldest = self.age
        elif other.age > other2.age and other.age > self.age:
            oldest = other.age
        else:
            oldest = other2.age
        
        print (f'The oldest cat is {oldest} years old')

cat1 = Cat('Fluffy', 2)
cat2 = Cat('Clawford', 8)
cat3
cat3 = Cat('Mittens', 5)