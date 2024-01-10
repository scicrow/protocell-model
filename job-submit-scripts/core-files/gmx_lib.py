#!/bin/python


import subprocess

#this is just an input for error handling to be implemented
file_name = __file__
file_list = file_name.split("/")
file_name = file_list[-1]
from make_sbatch import *

#coord_in to change after min, eq1, eq2, prod1, prod2

def make_index (file_name, run_type, coord_in):
   #Create index file. not needed for min step?
   commands = """
   r DCN
   r DCA | r DCN
   r SOL | r K  | r CL
   name 10 Water_and_ions
   q 
   """
   #shell=true necessary for this file format. otherwise, wont interpret this line as text.
   subprocess.run(f"echo '{commands}' | {run_type} make_ndx -f {coord_in} -o index.ndx", shell=True)



def inp_grompp (file_name, coord_in, top_in, mdp_in, deff_nm, rest_op):
    #handles the input parameters for grompp. forcefield and coords are hard-coded but mdp must be specified.
    
    par_list = ["-f", mdp_in, "-c", coord_in, "-p", top_in, "-o", deff_nm] #, rstrt_out, index_out]
    
    #command looks like gmx grompp -f min.mdp -c coord.pdb -p topology.top -o deffnm
    if rest_op == None:
        print ("No restraint file specified")
    
    else:
        par_list.extend(["-r", coord_in]) 
   
    print(par_list)
    return par_list



def run_grompp (file_name, run_type,  par_list, grompp_stage):
    
    args_list = [run_type, "grompp"]
    args_list.extend(par_list)
    #grompp_stage should be filled for everything except minimization runs. allows index generated for restraints and analysis
    if grompp_stage == None:
        print ("No index file input")
    else:
        args_list.extend(['-n', 'index.ndx'])
    try:
        subprocess.run(args_list)
        #needs clearer error handling
    except subprocess.CalledProcessError as e:
        print(' ProcessError in ' + file_name + ' run_grompp: {e}')
    except Exception as error:
        print(f'An unexpected error occured in ' + file_name + 
              ' run_grompp: {error}')


    
def run_mdrun (run_type, deff_input, job_type):
    # runs molecular dynamics from an input .tpr file generated in run_grompp. deff_nm should be formatted wihout the '.tpr'
    #feeds into make_sbatch.py
    sbatch_com = run_type + ' mdrun -deffnm ' + deff_input + ' -cpi -maxh 24.2'
    #print (sbatch_com)
    # dlb = dynamic load balancing. -cpi writes and looks for
    
    #check a job type was actually input, then create the sbatch file using make_sbatch.py
    if job_type != None:
        job_name, sb_copy = sbatch_copy(job_type) #copy sbatch template and rename the copy
        sbatch_jobname(job_name, sb_copy) #change the jobname field in the sbatch script
        sbatch_type(sbatch_com, sb_copy) #change the srun command in script

    else:
        print ("Failed to define job type! Quiting...") 
