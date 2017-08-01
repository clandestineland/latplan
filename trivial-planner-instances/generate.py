#!/usr/bin/env python3

import numpy as np
import os
import os.path
from scipy import misc
import sys
sys.path.append('../../')

def run_puzzle():
    import latplan.puzzles.puzzle_mnist as p
    p.setup()
    size = 3
    def convert(panels):
        return np.array([
            [i for i,x in enumerate(panels) if x == p]
            for p in range(size*size)]).reshape(-1)
    ics = [
        # from Reinfield '93
        convert([8,0,6,5,4,7,2,3,1]), # the second instance with the longest optimal solution 31
        convert([8,7,6,0,4,1,2,5,3]), # the first instance with the longest optimal solution 31
        convert([8,5,6,7,2,3,4,1,0]), # the first instance with the most solutions
        convert([8,5,4,7,6,3,2,1,0]), # the second instance with the most solutions
        convert([8,6,7,2,5,4,3,0,1]), # the "wrong"? hardest eight-puzzle from
        convert([6,4,7,8,5,0,3,2,1]), # w01fe.com/blog/2009/01/the-hardest-eight-puzzle-instances-take-31-moves-to-solve/
        convert([0, 1, 2, 3, 6, 8, 4, 7, 5]), # generated by ./randomwalk_instance_generator.py puzzle_mnist 20 10
        convert([4, 3, 1, 5, 6, 2, 7, 0, 8]),
        convert([4, 5, 7, 2, 6, 8, 1, 0, 3]),
        convert([2, 0, 5, 3, 1, 8, 7, 6, 4]),
        convert([8, 6, 0, 7, 3, 2, 4, 5, 1]),
        convert([6, 8, 2, 3, 4, 5, 1, 0, 7]),
        convert([4, 3, 6, 0, 2, 1, 7, 8, 5]),
        convert([8, 0, 1, 3, 6, 2, 5, 7, 4]),
        convert([6, 8, 3, 1, 2, 4, 0, 7, 5]),
        convert([4, 1, 8, 7, 3, 2, 0, 6, 5]),
        convert([3, 0, 1, 4, 5, 2, 6, 7, 8]), # generated by ./randomwalk_instance_generator.py puzzle_mnist 5 5
        convert([1, 2, 5, 0, 3, 4, 6, 7, 8]),
        convert([5, 1, 2, 0, 4, 8, 3, 6, 7]),
        convert([3, 0, 2, 6, 1, 5, 7, 4, 8]),
        convert([5, 1, 2, 0, 7, 4, 3, 6, 8]),
    ]

    from latplan.randomwalk_instance_generator import puzzle_mnist
    ics = [ convert(c) for c in puzzle_mnist(4, 100) ]
    
    gcs = [convert([0,1,2,3,4,5,6,7,8])]

    for i,init in enumerate(p.generate(ics,size,size)):
        for j,goal in enumerate(p.generate(gcs,size,size)):
            d = "{}/{}-{}".format(p.__name__,i,j)
            os.makedirs(d)
            misc.imsave(os.path.join(d,"init.png"),init)
            misc.imsave(os.path.join(d,"goal.png"),goal)
        
# def run_lightsout(path, network, p):
#     size = 4
#     from model import GumbelAE
#     ae = default_networks[network](path)
#     configs = np.array(list(p.generate_configs(size)))
#     ig_c = [[0,1,0,0,
#              0,1,0,0,
#              0,0,1,1,
#              1,0,0,0,],
#             np.zeros(size*size)]
#     ig = p.states(size,ig_c)
# 
# def run_lightsout3(path, network, p):
#     size = 3
#     from model import GumbelAE
#     ae = default_networks[network](path)
#     configs = np.array(list(p.generate_configs(size)))
#     ig_c = [[0,0,0,
#              1,1,1,
#              1,0,1,],
#             np.zeros(size*size)]
#     ig = p.states(size,ig_c)
# 
# def run_hanoi(path, network, p, disks=4):
#     from model import GumbelAE
#     ae = default_networks[network](path)
#     configs = np.array(list(p.generate_configs(disks)))
#     ig_c = np.zeros((2,disks),dtype=np.int8)
#     ig_c[1,:] = 2
#     ig = p.states(disks,ig_c)

run_puzzle()
