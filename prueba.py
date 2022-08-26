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
		self.weight -= 0.2

conejito = Rabbit("cone", 1)
print(f"{conejito.weight}")
conejito.eat()
print(f"{conejito.weight}")

for i in range (10):
	conejito.noeat()
	print(f"{conejito.name} didn´t eat")
	print(f"{conejito.weight}")

