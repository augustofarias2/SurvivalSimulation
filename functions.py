import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.animation import FuncAnimation
import copy

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
