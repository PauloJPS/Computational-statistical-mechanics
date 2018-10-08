#Simple implementation of conway's game of life

import numpy as np
import matplotlib.pyplot as plt
import os


def initial_config(size, pattern):
    lattice = np.zeros((size, size))
    ini = int(size/2)
    if pattern == 'blinkers':
        lattice[ini, ini-1] = 1
        lattice[ini, ini] = 1
        lattice[ini, ini+1] = 1
    elif pattern == 'gliders':
        lattice[ini, ini-1] = 1
        lattice[ini, ini] = 1
        lattice[ini, ini+1] = 1
        lattice[ini+1,ini-1] = 1
        lattice[ini+2, ini] = 1
    elif pattern == 'bote':
        lattice[ini, ini-1] = 1
        lattice[ini, ini] = 1
        lattice[ini+1, ini+1] = 1
        lattice[ini+1,ini-1] = 1
        lattice[ini+2, ini] = 1
    elif pattern == 'sapo':
        lattice[ini, ini-1] = 1
        lattice[ini, ini] = 1
        lattice[ini, ini+1] = 1
        lattice[ini+1, ini-2] = 1
        lattice[ini+1, ini-1] = 1
        lattice[ini+1, ini] = 1
    elif pattern == 'lwss':
        lattice[ini-1, ini-1] = 1
        lattice[ini-1, ini+2] = 1
        lattice[ini, ini-2] = 1
        lattice[ini+1, ini-2] = 1
        lattice[ini+1, ini+2] = 1
        lattice[ini+2, ini-2] = 1
        lattice[ini+2, ini-1] = 1
        lattice[ini+2, ini] = 1
        lattice[ini+2, ini+1] = 1
    elif pattern == 'acorn':
        lattice[ini-1, ini-2] = 1
        lattice[ini, ini] = 1
        lattice[ini+1, ini-3] = 1
        lattice[ini+1, ini-2] = 1
        lattice[ini+1, ini+1] = 1
        lattice[ini+1, ini+2] = 1
        lattice[ini+1, ini+3] = 1
    elif pattern == 'exploder':
        lattice[ini-2, ini-2] = 1
        lattice[ini-2, ini] = 1
        lattice[ini-2, ini+2] = 1

        lattice[ini-1, ini-2] = 1
        lattice[ini-1, ini+2] = 1

        lattice[ini, ini-2] = 1
        lattice[ini, ini+2] = 1

        lattice[ini+1, ini-2] = 1
        lattice[ini+1, ini+2] = 1

        lattice[ini+2, ini-2] = 1
        lattice[ini+2, ini] = 1
        lattice[ini+2, ini+2] = 1



 
    else:
        lattice = 1*(np.random.rand(size,size) < 0.1)
    return lattice

def neighborhood(lattice, size, i, j):
    aux = 0
    for k in range(-1,2):
        for w in range(-1,2):
            if k==0 and w==0:
                continue
            else: aux += lattice[(i+k)%size, (j+w)%size]
    return aux

def temporal_evolution(lattice, size, times):
    lattices = []

    plt.matshow(lattice)
    plt.savefig('0.png', format='png')
    plt.close()
    for t in range(1,times+1):
        live_x = []
        live_y = []
        die_x = []
        die_y = []
        for i in range(size):
            for j in range(size):
                num_neig = neighborhood(lattice, size, i,j)
                if num_neig == 2 and lattice[i,j]==1:
                    live_x.append(i) 
                    live_y.append(j) 
                elif num_neig == 2 and lattice[i,j]==0:
                    die_x.append(i) 
                    die_y.append(j) 
                elif num_neig == 3:
                    live_x.append(i) 
                    live_y.append(j) 
                else: 
                    die_x.append(i)
                    die_y.append(j)
        lattice[live_x, live_y] = 1
        lattice[die_x, die_y] = 0
        plt.matshow(lattice)
        plt.savefig('%d.png'%t, format='png')
        plt.close()

def breath_of_life(size, times, pattern):
    lattice = initial_config(size, pattern)
    temporal_evolution(lattice, size, times)
    os.system('ffmpeg -r 5 -i %%d.png -f mp4 -q:v 0 -vcodec mpeg4  conways_movie_%s.mp4'%pattern)
    os.system('rm *.png')

