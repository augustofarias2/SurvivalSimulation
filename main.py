import numpy as np
import random

from prueba import *

x=int(input("Choose x size\n"))
y=int(input("Choose y size\n"))

zone=np.ones((x,y))
movement=["u","d","l","r"]
rabbit = Rabbit("rabbit", 1)
pos=(int(x/2),int(y/2))
print(zone[(2, 2)])

while rabbit.weight>0:
	mov=random.choice(movement)
	print (zone(pos))
	if mov="u"

