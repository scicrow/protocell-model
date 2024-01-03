#!/bin/python


import subprocess
import datetime
file_name = __file__
file_list = file_name.split("/")
file_name = file_list[-1]
#print(file_name)


def inp_grompp (file_name, mdp_in):
    #handles the input parameters for grompp. forcefield and coords are hard-coded but mdp must be specified.
    deff_nm = mdp_in.split(".")[0] #naming scheme for the run used by gmx in next step
    
    #hardcoding variables at the moment. future idea would be good to is to make these defaults, then change if not existing
    coord_in = "L21hybrid_bilayer_100mM_Kions.pdb"
    top_in = "L21hybrid_bilayer_Kions_topol.top"

    #some runs should have restart and index outputs. may need a separate function for grompp with index?


    #par_list can just become in_list in future versions of code. This is just a hacky addition to earlier editions
    par_list = ["-f", mdp_in, "-c", coord_in, "-p", top_in, "-o", deff_nm] #, rstrt_out, index_out]
    #command looks like gmx grompp -f min.mdp -c coord.pdb -p topology.top -o deffnm
    
    #print(par_list)
    #print(deff_nm)
    return par_list



#error checking for list names that isn't useful for the moment.

    # check list length. only appropriate if feeding the whole list in
#    if len(in_list) < 4:
#        er_msg = ['Error running grompp. must have 4-6 arguments. ' +
#                  'Check ' + file_name + ' inp_grompp for info']	
#        print(er_msg)
#        return 1

#    if len(in_list) > 4:
#        rstrt_out = (in_list[4] + '  -r ')
#    if len(in_list) > 5:
#        index_out = (in_list[5] + ' -n ')



def run_grompp (file_name, par_list):
    
    gromacs_type = "gmx_mpi_d" #use gmx if not on setonix
    args_list = [gromacs_type, "grompp"]
    args_list.extend(par_list)
    #print (args_list)		 
    try:
        #subprocess.run("cd ..")
        subprocess.run(args_list)
        #needs clearer error handling
    except subprocess.CalledProcessError as e:
        print(' ProcessError in ' + file_name + ' run_grompp: {e}')
    except Exception as error:
        print(f'An unexpected error occured in ' + file_name + 
              ' run_grompp: {error}')
    


def run_mdrun (file_name, tpr_input, max_hour):
    # runs molecular dynamics from an input .tpr file generated in run_grompp. replace gmx_mpi_d with gmx for non-parallelised runs
    run_type = "gmx_mpi_d"
    subprocess.run([run_type, 'mdrun', '-deffnm', tpr_input, '-cpi', '-maxh', max_hour])
    # dlb = dynamic load balancing. -cpi writes and looks for





#each one of the below will become a run function at some point. they have been used individually to success

par_list = (inp_grompp(file_name, "en_min.mdp"))
#run_grompp(file_name, par_list)
#inp_list = [file_name, "en_min", "24.2"]
run_mdrun(*inp_list)
#print (inp_list)



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
