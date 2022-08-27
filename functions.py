import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.animation import FuncAnimation
import copy
import random

def eating(pos,zone,rabbit):
    if 	zone[pos]==1:
        rabbit.eat()
        zone[pos]=0
    elif zone[pos]==0:
        rabbit.noeat()
        
def plot_zone(zone,pos):
    map=copy.deepcopy(zone)
    map[pos]=2
    cmap = LinearSegmentedColormap.from_list('my_cmap', ['brown', 'green', 'white'])
    plt.imshow(X=map, cmap=cmap)
    plt.show()

def movimiento(a,b,pos,x,y,moves):
    movement=["u","d","l","r"]
    mov=random.choice(movement)
    moves.append(mov)
    if mov=="d" and (pos[0]+1)!=x:
        a=pos[0]+1
    if mov=="u" and (pos[0]-1)!=-1:
        a=pos[0]-1
    if mov=="r" and (pos[1]+1)!=y:
        b=pos[1]+1
    if mov=="l" and (pos[1]-1)!=-1:
        b=pos[1]-1
    pos=(a,b); return pos,a,b