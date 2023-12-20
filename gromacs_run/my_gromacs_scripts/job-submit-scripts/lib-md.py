#!/bin/python

import subprocess
import datetime
file_name = __file__
file_list = file_name.split("/")
file_name = file_list[-1]
#print(file_name)


#  name script

# look at molecule, generate topology 

# minimization script

#def pdb_amber():
#	return 0
	
def name_function(name_pdb): # should be a function for checking name. INCOMPLETE 
# originall done for amber and this needs to be moved to gromacs
	# subprocess.run(["if [ -z " + name_pdb + " ] && read -p 'enter a file name...' # at some point I should finish this bit

	name_list = name_pdb.split(".")
	name = name_list[0]
	print(name)
	
	name_array=[name + '.prmtop', name + '.inpcrd', name + '_resrt.ncrst', 
	name + '_heat.ncrst', name + '_prod.nc'] 
	# name_array="input topology", "input coordinate", 
	# "minimization restart", "heat restart", "prod trajectory" 
	return name_array



def inp_grompp (file_name, in_str):
	#handles the input parameters for grompp
	#prepare a list from input and check its length.
	in_list = in_str.split(",")
	if len(in_list) < 4:
		er_msg = ['Error running grompp. must have 4-6 arguments. ' + 
			'Check ' + file_name + ' inp_grompp for info']	
		print(er_msg)
		return 1
	
	mdp_in = ('-f ' + in_list[0]) 
	coord_in = ('-c' + in_list[1])
	top_in = ('-p' + in_list[2])
	tpr_out = ('-o' + in_list[3])

	#some runs should have restart and index outputs. below handles this
	# maybe just figure this bit out later. 
	#restrt_out = None
	#index_out = None

	if len(in_list) > 4:
		rstrt_out = (in_list[4] + '  -r ')
	if len(in_list) > 5:
		index_out = (in_list[5] + ' -n ')
	
	par_list = [mdp_in, coord_in, top_in, tpr_out] #, rstrt_out, index_out]
	#some values will be None, which must be cleaned with correct position
	#print(par_list)
		
	return par_list




def run_grompp (file_name, run_type, par_list):
		#note to self: try actually runs the command
		#runs grompp based on an inp_grompp list. restart and index files are an issue
		args_list = [run_type]
		args_list.extend(par_list)
		#print (args_list)		 
		try:
			subprocess.run(args_list)
			#needs clearer error handlimg
		except subprocess.CalledProcessError as e:
			print(' ProcessError in ' + file_name + ' run_grompp: {e}')
		except Exception as e:
			print(f'An unexpected error occured in ' + file_name + 
			' run_grompp: {e}')



def run_mdrun (filename, run_type, dlb_stat, tpr_input, max_hour):
	# runs molecular dynamics from an input .tpr file generated in run_grompp. replace gmx_mpi_d with gmx for non-parallelised runs
	subprocess.run ([run_type, 'mdrun', '-dlb',dlb_stat , '-deffnm', tpr_input, '-cpi', '-maxh', max_hour ])
	# dlb = dynamic load balancing. -cpi writes and looks for



def debug_run ():
	subprocess.run(['echo hello world'], shell=True, text=True)













#JUNK
#def run_MD(md_in):
	
	#try:
#	sander_cmd = [
#	"sander "
#	"-O ",  # write output files
#	"-i " + md_in[0],
#	"-o " + md_in[1] + "_md.out", # output file
#	"-p " + md_in[2], # amber topology file
#	"-c " + md_in[3], # amber coordinate file
#	"-r " + md_in[4], # restart coordinate file, used in next stage
#	"-x " + "out_" + md_in[0] + ".mdcrd", # restard coordinate file
#	"-inf " + "out_" + md_in[1] + ".mdinfo" # information file
#	]
#		
#	print (sander_cmd)
#	#except subprocess.CalledProcessError as e:
#		# when command fails
#	#	print ("Error: " + e.returncode) 
#	#	print (e.output)
#	# need the subprocess command here too. 
#	return 0
#
#
## subprocess.run([run_type, '-O -i 01_min.in -o 01_min.out -p ' ])
#
## 'pmemd.MPI -O -i 01_min.in -o 01_min.out -p ${in_array[0]} -c ${in_array[1]} -r ${in_array[2]} -inf 01_min.mdinf'
#
#def minimize_conf(md_in):
#	
#	subprocess.run(
#	# need a min.in min.out, topology, coord, restart and info
#	return 0
#
#def name_conf(pdb_in):
#
#	date_n = datetime.datetime.now().strftime('-%m%d%H%M')
#	return date_n
#
#
## heating script
#
## production script
#
## analysis script
#
## run command??
#
#
## md_test_list = ["one", "two", "three", "cat", "bacone", "sausage"]
#
## run_MD(md_list)
#
##now_is = name_conf(pdb_in)
##print(now_is)
