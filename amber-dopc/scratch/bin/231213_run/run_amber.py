#!/usr/bin/python
# script for running an amber simulation
# import array handling, pmemd, sander, ambertools, sys? 
import sys
import subprocess
# import array as arr # might not actually be needed

run_type="sander"



def name_function(name_pdb):
	name_list = name_pdb.split(".")
	name = name_list[0]
	print(name)
	
	name_array=[name + '.prmtop', name + '.inpcrd', name + '_resrt.ncrst', name + '_heat.ncrst', name + '_prod.nc'] 
	# name_array="input topology", "input coordinate", "minimization restart", "heat restart", "prod trajectory" 
	return name_array



def run_minimization(in_array, run_type):
#	print(in_array)
#	subprocess.run(["echo" + " 'Hi this is your output'"], shell=True) 

	subprocess.run([run_type + " -O -i 01_min.in -o 01_min.out -p " + in_array[0] + " -c " + in_array[1] + " -r " + in_array[2] + " -inf 01_min.mdinfo "], shell=True)


def run_heating (in_array):
	print()

def run_prod (in_array):
	print()


name_array=name_function("dopc128x1_42w_lipid21.pdb")
run_minimization(name_array, run_type)

