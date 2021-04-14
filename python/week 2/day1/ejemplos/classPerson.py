class Person:
	def __init__(self, name, age=0):
		self.name = name
		self.age = age
		self.skills = []
	def say_hello(self):
		print(f"Hi, my name is {self.name} I'm {self.age} years old.")
		print("I'm good at", ",".join(self.skills))
	def have_birthday(self):
		self.age += 1
	def learn_something(self, thing):
		self.skills.append(thing)
# All methods must have self as param 1.
# init... attach variable to self.