#!/bin/python

import subprocess
import datetime

# name script

# look at molecule, generate topology 

# minimization script

def pdb_amber():
	return 0
	
def name_function(name_pdb): # should be a function for checking name. INCOMPLETE
	# subprocess.run(["if [ -z " + name_pdb + " ] && read -p 'enter a file name...' # at some point I should finish this bit

	name_list = name_pdb.split(".")
	name = name_list[0]
	print(name)
	
	name_array=[name + '.prmtop', name + '.inpcrd', name + '_resrt.ncrst', 
	name + '_heat.ncrst', name + '_prod.nc'] 
	# name_array="input topology", "input coordinate", 
	# "minimization restart", "heat restart", "prod trajectory" 
	return name_array


def run_MD(md_in):
	
	#try:
	sander_cmd = [
	"sander "
	"-O ",  # write output files
	"-i " + md_in[0],
	"-o " + md_in[1] + "_md.out", # output file
	"-p " + md_in[2], # amber topology file
	"-c " + md_in[3], # amber coordinate file
	"-r " + md_in[4], # restart coordinate file, used in next stage
	"-x " + "out_" + md_in[0] + ".mdcrd", # restard coordinate file
	"-inf " + "out_" + md_in[1] + ".mdinfo" # information file
	]
		
	print (sander_cmd)
	#except subprocess.CalledProcessError as e:
		# when command fails
	#	print ("Error: " + e.returncode) 
	#	print (e.output)
	# need the subprocess command here too. 



# subprocess.run([run_type, '-O -i 01_min.in -o 01_min.out -p ' ])

# 'pmemd.MPI -O -i 01_min.in -o 01_min.out -p ${in_array[0]} -c ${in_array[1]} -r ${in_array[2]} -inf 01_min.mdinf'

def minimize_conf(md_in):
	
	subprocess.run(
	# need a min.in min.out, topology, coord, restart and info
	return 0

def name_conf(pdb_in):

	date_n = datetime.datetime.now().strftime('-%m%d%H%M')
	return date_n


# heating script

# production script

# analysis script

# run command??


# md_test_list = ["one", "two", "three", "cat", "bacone", "sausage"]

# run_MD(md_list)

now_is = name_conf(pdb_in)
print(now_is)
