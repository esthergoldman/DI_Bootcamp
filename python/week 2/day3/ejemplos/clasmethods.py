class Circle:
	PI = 3.14159265
	count = 0
	def __init__(self, radius):
		self.radius = radius
		Circle.count += 1
	@property   # GETTER (You can also look up SETTER)
	def area(self):
		return Circle.PI * self.radius**2
	def circumference(self, radius):
		return Circle.PI * self.radius*2
	@classmethod
	def getpi(cls):
		return cls.PI
	@staticmethod
	def info(how_many_times):
		for i in range(how_many_times):
			print("A circle is a shape consisting of all points in a plane that are a given distance from a given point, the centre")