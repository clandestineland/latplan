#!/bin/bash
./plan.py mands 'run_puzzle("samples/mnist_puzzle33p_fc2","fc2",import_module("puzzles.mnist_puzzle"),init=3)' |& tee $(dirname $0)/mands-mnist3.log
