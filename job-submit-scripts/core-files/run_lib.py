#!/bin/python
#run_lib.py 08/01/2024 thomas crow. a library to run each step of a gromacs simulations. minimization, equilibration and production. uses gromacs_lib.py which must be in same dir.
#mdp, coord topology, and itp forcefields should all be included in the same directory

import sys
import subprocess

try:
    from gmx_lib import *
except:
    print("gmx_lib not found. ensure it is in the same dir as run_lib")


#this is just an input for error handling to be implemented
file_name = __file__
file_list = file_name.split("/")
file_name = file_list[-1]

#input defined by mdx.sh. [0] is run_lib.py [1] is the input par [2] and [3] are pathnames
usr_in = sys.argv[1].lower()
run_type = sys.argv[2].lower() #gmx or gmx_mpi_d
core_dir = sys.argv[3]
core_path = core_dir + "/"
run_dir = sys.argv[4] 


def run_step(usr_in):
    #defines which stage of the simulation you are running, from position 1 of the input argument
    print("run_lib.py 08/01/2024 a script for running gromacs. user input required to determine step: min/eq1/eq2/295/305 \n")
    if usr_in == 'min':
        minimization_run(run_type, coord_in, top_in, core_path)
        run_mdrun(run_type, "en_min", "min", core_dir, run_dir) #run type, tpr file, job type for sbatch
    elif usr_in == 'eq1':
        eq1_run(run_type, top_in, core_path)
        run_mdrun(run_type, "premd1", "eq1", core_dir, run_dir)
    elif usr_in == 'eq2':
        eq2_run(run_type, top_in, core_path)
        run_mdrun(run_type, "premd2", "eq2", core_dir, run_dir)
    elif usr_in == '295':
        prod295_run(run_type, top_in, core_path)
        run_mdrun(run_type, "md_295", "295", core_dir, run_dir)
    elif usr_in == '305':
        prod305_run(run_type, top_in, core_path)
        run_mdrun(run_type, "md_305", "305", core_dir, run_dir)
    else:
        print ('Incorrect input. please enter min/eq1/eq2/295 or 305.')



def minimization_run(run_type, coord_in, top_in, run_dir):
    mdp_in = run_dir + "en_min.mdp" 
    deff_nm = mdp_in.split(".")[0] #naming scheme for the run used by gmx in next step
    rest_op = None
    input_list = [coord_in, top_in, mdp_in, deff_nm, rest_op]
    grompp_stage = 0

    make_index(file_name, run_type, coord_in)
    grompp_input = inp_grompp(file_name, *input_list)
    run_grompp(file_name, run_type, grompp_input, grompp_stage)


#equilibration with restraints on lipid bilayer

def eq1_run(run_type, top_in, run_dir):
    coord_in = "en_min.gro"
    mdp_in = run_dir + "premd1.mdp" 
    deff_nm = mdp_in.split(".")[0] #naming scheme for the run used by gmx in next step
    tpr_input = deff_nm + ".tpr"
    rest_op = coord_in
    input_list = [coord_in, top_in, mdp_in, deff_nm, rest_op]
    grompp_stage = "eq"

    grompp_input = inp_grompp(file_name, *input_list)
    make_index(file_name, run_type, coord_in)
    run_grompp(file_name, run_type, grompp_input, grompp_stage)


#removing restraint and continue equilibration

def eq2_run(run_type, top_in, run_dir):
    coord_in = "premd1.gro"
    mdp_in = run_dir + "premd2.mdp" 
    deff_nm = mdp_in.split(".")[0] #naming scheme for the run used by gmx in next step
    tpr_input = deff_nm + ".tpr"
    rest_op = "No"
    input_list = [coord_in, top_in, mdp_in, deff_nm, rest_op]
    grompp_stage = "eq" 

    grompp_input = inp_grompp(file_name, *input_list)
    make_index(file_name, run_type, coord_in)
    run_grompp(file_name, run_type, grompp_input, grompp_stage)


#heating to 295K

def prod295_run(run_type, top_in, run_dir):
    coord_in = "premd2.gro"
    mdp_in = run_dir + "md_295.mdp" 
    deff_nm = mdp_in.split(".")[0] #naming scheme for the run used by gmx in next step
    rest_op = "No"
    input_list = [coord_in, top_in, mdp_in, deff_nm, rest_op]
    grompp_stage = True

    grompp_input = inp_grompp(file_name, *input_list)
    make_index(file_name, run_type, coord_in)
    run_grompp(file_name, run_type, grompp_input, grompp_stage)


#heating to 305K

def prod305_run(run_type, top_in, run_dir):
    coord_in = "md_295.gro"
    mdp_in = "md_305.mdp"
    deff_nm = mdp_in.split(".")[0] #naming scheme for the run used by gmx in next step
    rest_op = "No"
    input_list = [coord_in, top_in, mdp_in, deff_nm, rest_op]
    grompp_stage = True

    grompp_input = inp_grompp(file_name, *input_list)
    make_index(file_name, run_type, coord_in)
    run_grompp(file_name, run_type, grompp_input, grompp_stage)



#MD RUN MANAGEMENT COMMANDS

#finds the initial pdb and top files for minimization run
coord_in, top_in = find_pdb(core_dir)
run_step(usr_in)
