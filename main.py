import numpy as np
from classes import *
from functions import *

x=int(input("Choose x size\n"))
y=int(input("Choose y size\n"))

zone=np.ones((x,y))

rabbit = Rabbit("Rabbit", 1)
a=int(x/2)
b=int(y/2)
pos=(a,b)
iter=0
eating(pos,zone,rabbit)
moves=[]

while rabbit.weight>0:
	pos,a,b=movimiento(a,b,pos,x,y,moves)
	eating(pos,zone,rabbit)

print(f"{rabbit.name} is dead")
plot_zone(zone,pos)
print(moves)