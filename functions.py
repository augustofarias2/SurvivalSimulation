import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.animation import FuncAnimation
import time

def eating(pos,zone,rabbit):
    if 	zone[pos]==1:
        rabbit.eat()
        zone[pos]=0
    elif zone[pos]==0:
        rabbit.noeat()
        
def plot_zone(zone):
    cmap = LinearSegmentedColormap.from_list('my_cmap', ['brown', 'green'])
    plt.imshow(X=zone, cmap=cmap)
    plt.show()

