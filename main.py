import numpy as np
import random
from classes import *
from functions import *

x=int(input("Choose x size\n"))
y=int(input("Choose y size\n"))

zone=np.ones((x,y))
movement=["u","d","l","r"]
rabbit = Rabbit("Rabbit", 1)
a=int(x/2)
b=int(y/2)
pos=(a,b)
iter=0
eating(pos,zone,rabbit)
moves=[]

while rabbit.weight>0:
	mov=random.choice(movement)
	moves.append(mov)
	if mov=="d" and (pos[0]+1)!=x:
		a=pos[0]+1
	if mov=="u" and (pos[0]-1)!=-1:
		a=pos[0]-1
	if mov=="r" and (pos[1]+1)!=y:
		b=pos[1]+1
	if mov=="l" and (pos[1]-1)!=0-1:
		b=pos[1]-1
	pos=(a,b)
	eating(pos,zone,rabbit)
	plot_zone(zone,pos)

print(moves)