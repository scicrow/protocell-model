#!/bin/python
#run_lib.py 08/01/2024 thomas crow. a library to run each step of a gromacs simulations. minimization, equilibration and production. uses gromacs_lib.py which must be in same dir.
#mdp, coord topology, and itp forcefields should all be included in the same directory

#import glob
import sys
from gmx_lib import *
import subprocess
import glob

#this is just an input for error handling to be implemented
file_name = __file__
file_list = file_name.split("/")
file_name = file_list[-1]

core_dir = sys.argv[3]
core_coord = glob.glob(f"{core_dir}/*.pdb")
core_coord = core_coord[0]
print(core_coord)
run_type = "gmx"
#run_type = "gmx_mpi_d" #for when on supercomputer
top_in = core_dir + ".top"
#top_in = "L21hybrid_bilayer_Kions_topol.top"
#topology and pdb file should be included in the same directory as this file.

#minimization run

def minimization_run(run_type, top_in):
    coord_in = ".pdb"
    #coord_in = "L21hybrid_bilayer_100mM_Kions.pdb"
    mdp_in = "en_min.mdp" 
    deff_nm = mdp_in.split(".")[0] #naming scheme for the run used by gmx in next step
    rest_op = None
    input_list = [coord_in, top_in, mdp_in, deff_nm, rest_op]
    grompp_stage = 0

    make_index(file_name, run_type, coord_in)
    grompp_input = inp_grompp(file_name, *input_list)
    run_grompp(file_name, run_type, grompp_input, grompp_stage)


#equilibration with restraints on lipid bilayer

def eq1_run(run_type, top_in):
    coord_in = "../en_min.gro"
    mdp_in = "premd1.mdp" 
    deff_nm = mdp_in.split(".")[0] #naming scheme for the run used by gmx in next step
    tpr_input = deff_nm + ".tpr"
    rest_op = coord_in
    input_list = [coord_in, top_in, mdp_in, deff_nm, rest_op]
    grompp_stage = "eq"

    grompp_input = inp_grompp(file_name, *input_list)
    make_index(file_name, run_type, coord_in)
    run_grompp(file_name, run_type, grompp_input, grompp_stage)


#removing restraint and continue equilibration

def eq2_run(run_type, top_in):
    coord_in = "../premd1.gro"
    mdp_in = "premd2.mdp" 
    deff_nm = mdp_in.split(".")[0] #naming scheme for the run used by gmx in next step
    tpr_input = deff_nm + ".tpr"
    rest_op = None
    input_list = [coord_in, top_in, mdp_in, deff_nm, rest_op]
    grompp_stage = True 

    grompp_input = inp_grompp(file_name, *input_list)
    make_index(file_name, run_type, coord_in)
    run_grompp(file_name, run_type, grompp_input, grompp_stage)


#heating to 295K

def prod295_run(run_type, top_in):
    coord_in = "../premd2.gro"
    mdp_in = "md_295.mdp" 
    deff_nm = mdp_in.split(".")[0] #naming scheme for the run used by gmx in next step
    rest_op = None
    input_list = [coord_in, top_in, mdp_in, deff_nm, rest_op]
    grompp_stage = True

    grompp_input = inp_grompp(file_name, *input_list)
    make_index(file_name, run_type, coord_in)
    run_grompp(file_name, run_type, grompp_input, grompp_stage)


#heating to 305K

def prod305_run(run_type, top_in):
    coord_in = "md_295.gro"
    mdp_in = "md_305.mdp"
    deff_nm = mdp_in.split(".")[0] #naming scheme for the run used by gmx in next step
    rest_op = None
    input_list = [coord_in, top_in, mdp_in, deff_nm, rest_op]
    grompp_stage = True

    grompp_input = inp_grompp(file_name, *input_list)
    make_index(file_name, run_type, coord_in)
    run_grompp(file_name, run_type, grompp_input, grompp_stage)




#the below doesn't sem to work well with sbatch

#pass the modelling stage in at command line. should be three-letter input with no spaces. 
#print("run_lib.py 08/01/2024 a script for running gromacs. user input required to determine step: min/eq1/eq2/295/305 \n")
#usr_in = sys.argv[1].lower()

#if usr_in == 'min':
#    minimization_run(run_type, top_in)
#    run_mdrun(run_type, "en_min")
#elif usr_in == 'eq1':
#eq1_run(run_type, top_in)
#run_mdrun(run_type, "premd1")
#elif usr_in == 'eq2':
#    eq2_run(run_type, top_in)
#    run_mdrun(run_type, "premd2")
#elif usr_in == '295':
#    prod295_run(run_type, top_in)
#    run_mdrun(run_type, "md_295")
#elif usr_in == '305':
#    prod305_run(run_type, top_in)
#    run_mdrun(run_type, "md_305")
#else:
#    print ('Incorrect input. please enter min/eq1/eq2/295 or 305.')


#analysis
