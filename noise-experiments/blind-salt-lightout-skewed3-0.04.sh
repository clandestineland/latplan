#!/bin/bash
./plan_noise.py blind 0.04 salt 'run_lightsout3 ( "samples/digital_lightsout_skewed3_fc"       ,"fc", import_module("puzzles.digital_lightsout_skewed"        ) )' |& tee $(dirname $0)/blind-salt-lightout-skewed3-0.04.log
