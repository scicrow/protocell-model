#!/bin/python

from pathlib import Path
import subprocess

#this is just an input for error handling to be implemented
file_name = __file__
file_list = file_name.split("/")
file_name = file_list[-1]
from make_sbatch import *
try:
    import glob
except:
    print("Error importing glob")

def find_pdb(core_dir):
    #a function for finding pdb file and topology file for the pdb run. there should be only one of each in the directory
    #if there are multiple, this function will pick the first one of each.

    #finds the coord file
    core_dir = str(core_dir)
    core_coord = glob.glob(f"{core_dir}/*.pdb")
    #cleans up the core_coord, so you don't need to see its directory path in messages.
    coord_address = core_coord[0]
    coord_name = coord_address.split("/")
    coord_name = coord_name[-1]

    if len(core_coord)>=2:
        print(f"multiple pdb files {len(core_coord)} detected. using {coord_name}")
    else:
        print(f"using {coord_name}")

    #core_coord = core_coord[0]

    #finds core directory topology file
    core_top = glob.glob(f"{core_dir}/*.top")
    
    #cleans up the core_top
    top_address = core_top[0]
    top_name = top_address.split("/")
    top_name = top_name[-1]

    if len(core_top)>=2:
        print(f"multiple pdb files {len(core_top)} detected. using {top_name}")
    else:
        print(f"using {top_name}")

    return(coord_address, top_address) 



def make_index (file_name, run_type, coord_in):
   #Create index file. not needed for min step? must be Cl K Na not all caps for ion names
   commands = """
   r LAU
   r LAUP | r LAU
   r SOL | r K  | r CL
   name 10 Water_and_ions
   q 
   """
   index_name = "index.ndx"
   #shell=true necessary for this file format. otherwise, wont interpret this line as text.
   subprocess.run(f"echo '{commands}' | {run_type} make_ndx -f {coord_in} -o {index_name}", shell=True)



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
    if grompp_stage == "No":
        print ("No index file input")
    else:
        args_list.extend(['-n', 'index.ndx'])
    #try:
    subprocess.run(args_list)
    print(args_list) 
    print(" is now running from run_grompp")
        #needs clearer error handling
    #except subprocess.CalledProcessError as e:
    #    print(' ProcessError in ' + file_name + ' run_grompp: {e}')
    #except Exception as error:
     #   print(f'An unexpected error occured in ' + file_name + 
      #        ' run_grompp: {e}')


    
def run_mdrun (run_type, deff_input, job_type, core_path, run_path):
    # runs molecular dynamics from an input .tpr file generated in run_grompp. deff_nm should be formatted wihout the '.tpr'
    #feeds into make_sbatch.py
    sbatch_input = run_type + ' mdrun -deffnm ' + deff_input + ' -cpi -maxh 24.2'
    #print (sbatch_com)
    # dlb = dynamic load balancing. -cpi writes and looks for
    
    #check a job type was actually input, then create the sbatch file using make_sbatch.py
    if job_type != "No":
        job_name, sb_loc = sbatch_copy(run_type, run_path, core_path) #copy sbatch template and rename the copy #jobtype, rundir, coredir vars needed
        sbatch_jobname(run_type, sb_loc) #change the jobname field in the sbatch script
        sbatch_type(sb_loc, sbatch_input) #change the srun command in script

    else:
        print ("Failed to define run_mdrun job type! Quiting...") 




def run_gmx_min (run_type, deff_input, job_type, core_dir, run_dir): #job type and dir information not needed, but makes it easy to switch to run_mdrun function
    # a script that runs a gromacs mdrun session. useful for minimization or local PC runs
    #tpr_in = core_dir + deff_input + ".tpr"
    #print(tpr_in)
    subprocess.run([run_type, "mdrun", "-deffnm", deff_input, "-cpi", "-maxh", "24.2"])

