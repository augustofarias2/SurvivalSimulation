class Rabbit:

	def __init__(
		self, name, weight
	):
		self.name = name
		self.weight = weight

	def eat(self):
		self.weight += 0.1

	def noeat(self):
		self.weight -= 0.1