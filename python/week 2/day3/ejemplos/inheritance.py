Inheritance
  IS A TYPE OF
Composition
  HAS ONE OR MORE OF
class Person:
	def __init__(self, name, age, language):
class Language:
	def __init__(self, name, region, first_spoken_date):
class Superman(Person):
	def __init__(self, name, age, super_powers, planet)
lang = Language("English", "UK", "850BC")
p1 = Person("bob", 1, Language("Greek", "France", "2021"))
# SUPERMAN IS A PERSON: Therefore Superman inherits from Person
# SUPERMAN HAS A LANGUAGE
# PERSON HAS A LANGUAGE
# So Person is composed of a Language