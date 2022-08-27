class Rabbit:

	def __init__(
		self, name, weight
	):
		self.name = name
		self.weight = weight

	def eat(self):
		print(f"{self.name} is eating")
		self.weight += 0.1

	def noeat(self):
		print(f"{self.name} is not eating")
		self.weight -= 0.2