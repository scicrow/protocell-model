#!/usr/bin/python
# script for running an amber simulation
# import array handling, pmemd, sander, ambertools, sys? 
import sys
import subprocess
# import array as arr # might not actually be needed

run_type="sander"



def name_function(name_pdb):
	# subprocess.run(["if [ -z " + name_pdb + " ] && read -p 'enter a file name...' # at some point I should finish this bit

	name_list = name_pdb.split(".")
	name = name_list[0]
	print(name)
	
	name_array=[name + '.prmtop', name + '.inpcrd', name + '_resrt.ncrst', 
	name + '_heat.ncrst', name + '_prod.nc'] 
	# name_array="input topology", "input coordinate", 
	# "minimization restart", "heat restart", "prod trajectory" 
	return name_array



def run_minimization(in_array, run_type):
#	print(in_array)
#	subprocess.run(["echo" + " 'Hi this is your output'"], shell=True) 

	subprocess.run([run_type + " -i 01_min.in -o 01_min.out -p " + 
	in_array[0] + " -c " + in_array[1] + " -r " + 
	in_array[2] + " -inf 01_min.mdinfo "], shell=True)



def run_heating (in_array):

	subprocess.run([run_type + " -i 02_heat.in -o 02_heat.out -p " + 
	in_array[0] + " -c " + in_array[2] + " -r " + 
	in_array[3] + " -inf 02_heat.mdinfo "], shell=True)	
	#coord needs to be min restart file



def run_prod (in_array):
	
	subprocess.run([run_type + " -i 03_prod.in -o 03_prod.out -p " + 
	in_array[0] + " -c " + in_array[3] + " -r " + 
	in_array[4] + " -inf 03_prod.mdinfo "], shell=True)


name_in = input()
name_array = name_function(name_in)
run_minimization(name_array)

