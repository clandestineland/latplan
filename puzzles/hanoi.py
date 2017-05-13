#!/usr/bin/env python3

import numpy as np

# state encoding:
# XX each disk has an x-position and a y-position (counted from the bottom)
# 3 towers
# each tower has a sequence of numbers (disks)
# in the decreasing order
# for example,
# [[012345678][][]] is the initial state of the tower
# [[][][012345678]] is the goal state of the tower

# how to enumerate such thing:

# each disk has a position and it also defines the state
# but many/most positions are invalid?
# [0,2,1,2,1,0]
# no, since there is an implicit order that is enforced,
# the assignments of each disk to some tower defines the entire state
# [0,2,1,2,1,0] == [[05][24][13]]

# random config is available from np.random.randint(0,3,size)

def generate_configs(size=6):
    import itertools
    return itertools.product(range(3),repeat=size)

def config_state(config):
    disk_state =[[],[],[]]
    for disk,pos in enumerate(config):
        disk_state[pos].append(disk)
    return disk_state

def state_config(state):
    size = len(state[0]) + len(state[1]) + len(state[2])
    config = np.zeros(size,dtype=np.int8)
    for i in range(3):
        for disk in state[i]:
            config[disk] = i
    return config

def successors(config):
    from copy import deepcopy
    # at most 6 successors
    state = config_state(config)
    succ = []
    for i in range(3):
        for j in range(3):
            if j != i and state[i]:
                if not state[j] or state[j][0] > state[i][0]:
                    # pseudo code
                    copy = deepcopy(state)
                    disk = copy[i].pop(0)
                    copy[j].append(disk)
                    succ.append(state_config(copy))
    return succ

from .mnist import mnist
x_train, y_train, _, _ = mnist()
filters = [ np.equal(i,y_train) for i in range(10) ]
imgs    = [ x_train[f] for f in filters ]
panels  = [ imgs[0].reshape((28,28)) for imgs in imgs ]

panels[8] = imgs[8][3].reshape((28,28))
panels[1] = imgs[1][3].reshape((28,28))
panels.append(np.random.uniform(0,1,(28,28)))

panels = np.array(panels)

base = 14
stepy = panels[0].shape[0]//base
stepx = panels[0].shape[1]//base
panels = panels[:,::stepy,::stepx][:,:base,:base].round()

patterns = [
    [[0,0,0,0,0,0,0,0,],
     [0,0,0,0,0,0,0,0,],
     [0,0,0,0,0,0,0,0,],
     [0,0,0,0,0,0,0,0,],
     [0,0,0,0,0,0,0,0,],
     [0,0,0,0,0,0,0,0,],
     [0,0,0,0,0,0,0,0,],
     [0,0,0,0,0,0,0,0,],],
    [[1,1,0,0,1,1,0,0,],
     [1,1,0,0,1,1,0,0,],
     [0,0,1,1,0,0,1,1,],
     [0,0,1,1,0,0,1,1,],
     [1,1,0,0,1,1,0,0,],
     [1,1,0,0,1,1,0,0,],
     [0,0,1,1,0,0,1,1,],
     [0,0,1,1,0,0,1,1,],],
    [[1,0,0,0,1,0,0,0,],
     [0,1,0,0,0,1,0,0,],
     [0,0,1,0,0,0,1,0,],
     [0,0,0,1,0,0,0,1,],
     [1,0,0,0,1,0,0,0,],
     [0,1,0,0,0,1,0,0,],
     [0,0,1,0,0,0,1,0,],
     [0,0,0,1,0,0,0,1,],],
    [[0,0,0,0,0,0,0,0,],
     [0,1,1,1,0,0,0,0,],
     [0,1,1,1,0,0,0,0,],
     [0,1,1,1,0,0,0,0,],
     [0,0,0,0,1,1,1,0,],
     [0,0,0,0,1,1,1,0,],
     [0,0,0,0,1,1,1,0,],
     [0,0,0,0,0,0,0,0,],],
    [[0,0,0,1,0,0,0,1,],
     [0,0,1,0,0,0,1,0,],
     [0,1,0,0,0,1,0,0,],
     [1,0,0,0,1,0,0,0,],
     [0,0,0,1,0,0,0,1,],
     [0,0,1,0,0,0,1,0,],
     [0,1,0,0,0,1,0,0,],
     [1,0,0,0,1,0,0,0,],],
    [[0,0,0,1,1,0,0,0,],
     [0,0,1,0,0,1,0,0,],
     [0,1,0,0,0,0,1,0,],
     [1,0,0,0,0,0,0,1,],
     [0,0,0,1,1,0,0,0,],
     [0,0,1,0,0,1,0,0,],
     [0,1,0,0,0,0,1,0,],
     [1,0,0,0,0,0,0,1,],],
    [[1,0,0,0,0,0,0,1,],
     [0,1,0,0,0,0,1,0,],
     [0,0,1,0,0,1,0,0,],
     [0,0,0,1,1,0,0,0,],
     [1,0,0,0,0,0,0,1,],
     [0,1,0,0,0,0,1,0,],
     [0,0,1,0,0,1,0,0,],
     [0,0,0,1,1,0,0,0,],],
    [[0,0,0,0,0,0,0,0,],
     [0,0,0,0,1,1,1,0,],
     [0,0,0,0,1,0,1,0,],
     [0,0,0,0,1,1,1,0,],
     [0,1,1,1,0,0,0,0,],
     [0,1,0,1,0,0,0,0,],
     [0,1,1,1,0,0,0,0,],
     [0,0,0,0,0,0,0,0,],],
    [[1,0,0,0,1,0,0,0,],
     [1,0,0,0,1,0,0,0,],
     [0,1,0,0,0,1,0,0,],
     [0,1,0,0,0,1,0,0,],
     [0,0,1,0,0,0,1,0,],
     [0,0,1,0,0,0,1,0,],
     [0,0,0,1,0,0,0,1,],
     [0,0,0,1,0,0,0,1,],],
    [[0,0,0,1,0,0,0,1,],
     [0,0,0,1,0,0,0,1,],
     [0,0,1,0,0,0,1,0,],
     [0,0,1,0,0,0,1,0,],
     [0,1,0,0,0,1,0,0,],
     [0,1,0,0,0,1,0,0,],
     [1,0,0,0,1,0,0,0,],
     [1,0,0,0,1,0,0,0,],],
    [[1,0,1,0,1,0,1,0,],
     [1,0,1,0,1,0,1,0,],
     [1,0,1,0,1,0,1,0,],
     [1,0,1,0,1,0,1,0,],
     [1,0,1,0,1,0,1,0,],
     [1,0,1,0,1,0,1,0,],
     [1,0,1,0,1,0,1,0,],
     [1,0,1,0,1,0,1,0,],],
    [[1,1,1,1,1,1,1,1,],
     [0,0,0,0,0,0,0,0,],
     [1,1,1,1,1,1,1,1,],
     [0,0,0,0,0,0,0,0,],
     [1,1,1,1,1,1,1,1,],
     [0,0,0,0,0,0,0,0,],
     [1,1,1,1,1,1,1,1,],
     [0,0,0,0,0,0,0,0,],],
    [[0,0,0,0,0,0,0,0,],
     [0,0,0,0,0,0,0,0,],
     [1,1,1,1,1,1,1,1,],
     [1,1,1,1,1,1,1,1,],
     [1,1,1,1,1,1,1,1,],
     [1,1,1,1,1,1,1,1,],
     [0,0,0,0,0,0,0,0,],
     [0,0,0,0,0,0,0,0,],],
    [[0,0,1,1,1,1,0,0,],
     [0,0,1,1,1,1,0,0,],
     [0,0,1,1,1,1,0,0,],
     [0,0,1,1,1,1,0,0,],
     [0,0,1,1,1,1,0,0,],
     [0,0,1,1,1,1,0,0,],
     [0,0,1,1,1,1,0,0,],
     [0,0,1,1,1,1,0,0,],],
]

patterns = np.array(patterns)

def generate1(config):
    l = len(config)
    disk_size = 8
    disk_inc = disk_size // 2
    disk_height = disk_size
    base_disk_width_factor = 2
    base_disk_width = disk_size * base_disk_width_factor
    figure = np.ones([l*disk_height,(l*2*disk_inc+base_disk_width)*3+2],dtype=np.int8)
    state = config_state(config)
    # print(l,figure.shape)
    # print(config)
    # print(state)
    for i, tower in enumerate(state):
        tower.reverse()
        # print(i,tower)
        x_left  = (l*2*disk_inc+base_disk_width)*i     +   i
        x_right = (l*2*disk_inc+base_disk_width)*(i+1) + (i+1) - 1
        for j,disk in enumerate(tower):
            # print(j,disk,(l-j)*2)
            figure[
                (l-j-1)*disk_height:(l-j)*disk_height,
                x_left + (l-disk)*disk_inc : x_right - (l-disk)*disk_inc] \
                = 0
                # = np.tile(patterns[disk],(1,disk+base_disk_width_factor))
    return figure

def generate(configs):
    return np.array([ generate1(c) for c in configs ])
                

def states(size, configs=None):
    if configs is None:
        configs = generate_configs(size)
    return generate(configs)

def transitions(size, configs=None, one_per_state=False):
    if configs is None:
        configs = generate_configs(size)
    if one_per_state:
        def pickone(thing):
            index = np.random.randint(0,len(thing))
            return thing[index]
        transitions = np.array([
            generate([c1,pickone(successors(c1))])
            for c1 in configs ])
    else:
        transitions = np.array([ generate([c1,c2])
                                 for c1 in configs for c2 in successors(c1) ])
    return np.einsum('ab...->ba...',transitions)

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    def plot_image(a,name):
        plt.figure(figsize=(6,6))
        plt.imshow(a,interpolation='nearest',cmap='gray',)
        plt.savefig(name)
    def plot_grid(images,name="plan.png"):
        import matplotlib.pyplot as plt
        l = len(images)
        w = 6
        h = max(l//6,1)
        plt.figure(figsize=(20, h*2))
        for i,image in enumerate(images):
            # display original
            ax = plt.subplot(h,w,i+1)
            plt.imshow(image,interpolation='nearest',cmap='gray',)
            ax.get_xaxis().set_visible(False)
            ax.get_yaxis().set_visible(False)
        plt.savefig(name)
    disks = 6
    configs = generate_configs(disks)
    puzzles = generate(configs)
    print(puzzles.shape)
    print(puzzles[10])
    plot_image(puzzles[0],"hanoi.png")
    plot_grid(puzzles[:36],"hanois.png")
    _transitions = transitions(disks)
    print(_transitions.shape)
    import numpy.random as random
    indices = random.randint(0,_transitions[0].shape[0],18)
    _transitions = _transitions[:,indices]
    print(_transitions.shape)
    transitions_for_show = \
        np.einsum('ba...->ab...',_transitions) \
          .reshape((-1,)+_transitions.shape[2:])
    print(transitions_for_show.shape)
    plot_grid(transitions_for_show,"hanoi_transitions.png")
