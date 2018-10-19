import matplotlib.pyplot as plt
import numpy as np


def create_lattice(size):
    return np.zeros((size,size))

def left_site(lattice, size, x, y):
    if y == 0: return 0
    else: return 1

def right_site(lattice, size, x, y):
    if y == size-1: return 0
    else: return 1

def up_site(lattice, size, x, y):
    if x == 0: return 0
    else: return 1

def down_site(lattice, size, x, y):
    if x == size-1: return 0
    else: return 1

def dropping(lattice, size, threshold):
    counter = 0
    sites = []
    aux_sites = np.zeros((size, size))
    while(lattice.max() >= threshold):
        xs, ys = np.where(lattice >= threshold)
        for i in zip(xs, ys):
            lattice[i[0],i[1]] = 0 
            if left_site(lattice, size, i[0], i[1]):
                lattice[i[0], i[1]-1] += 1
            if right_site(lattice, size, i[0], i[1]):
                lattice[i[0], i[1]+1] += 1
            if up_site(lattice, size, i[0], i[1]):
                lattice[i[0]-1, i[1]] += 1
            if down_site(lattice, size, i[0], i[1]):
                lattice[i[0]+1, i[1]] += 1
        aux_sites[xs, ys] += 1
        counter += 1

    return counter,  np.count_nonzero(aux_sites), aux_sites.sum()

def exe(size, threshold, n_int):
    lattice = create_lattice(size)
    duration = []
    ava_len = []
    ava_total= []
    time = []
    count = 0
    for i in range(n_int):
        lattice[int(size/2), int(size/2)] += 1
        aux_c, aux_len, aux_total = dropping(lattice, size, threshold)
        if aux_c != 0:
            duration.append(aux_c)
            ava_len.append(aux_len)
            ava_total.append(aux_total)
    return np.array(duration), np.array(ava_len), np.array(ava_total), lattice

def plot(d, l, bins=100):
     plt.subplot(211)
     hist, bins = np.histogram(d, bins=bins)
     times = np.array([bins[:-1], hist])
     plt.scatter(np.log(times[0][times[1]!=0]), np.log(times[1][times[1]!=0]), label='data', s=10)
     a, b = np.polyfit(np.log(times[0][times[1]!=0]), np.log(times[1][times[1]!=0]), 1)
     plt.plot(np.log(times[0][times[1]!=0]), np.log(times[0][times[1]!=0])*a + b, label='fit - a=%.2f'%a)
     plt.xlabel('log(Duração da avalanche)', fontsize=15)
     plt.ylabel('log(frequencia)', fontsize=15)
     
     plt.legend()
 
     plt.subplot(212)    
     hist, bins = np.histogram(l, bins=bins)
     lens = np.array([bins[:-1], hist])                                              
     plt.scatter(np.log(lens[0][lens[1]!=0]), np.log(lens[1][lens[1]!=0]), label='data', s=10)
     a, b = np.polyfit(np.log(lens[0][lens[1]!=0]), np.log(lens[1][lens[1]!=0]), 1)
     plt.plot(np.log(lens[0][lens[1]!=0]), np.log(lens[0][lens[1]!=0])*a + b, label='fit - a=%.2f'%a)
     plt.xlabel('log(tamanho da avalanche)', fontsize=15)
     plt.ylabel('log(frequencia)', fontsize=15)
     plt.legend()
         
     
     plt.tight_layout()
     plt.savefig('sandpile.png', format='png')


