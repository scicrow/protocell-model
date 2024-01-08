#!/bin/python
#run_lib.py 08/01/2024 thomas crow. a library to run each step of a gromacs simulations. minimization, equilibration and production. uses gromacs_lib.py which must be in same dir.


from gmx_lib import *
import subprocess

#this is just an input for error handling to be implemented
file_name = __file__
file_list = file_name.split("/")
file_name = file_list[-1]

#coord_in to change after min, eq1, eq2, prod1, prod2

#run_type = "gmx"
run_type = "gmx"  #"gmx_mpi_d" #for when on supercomputer
top_in = "L21hybrid_bilayer_Kions_topol.top"

#each one of the below will become a run function at some point. they have been used individually to success

#minimization run

def minimization_run(run_type, top_in):
    coord_in = "L21hybrid_bilayer_100mM_Kions.pdb"
    mdp_in = "en_min.mdp" 
    deff_nm = mdp_in.split(".")[0] #naming scheme for the run used by gmx in next step
    rest_op = None
    input_list = [coord_in, top_in, mdp_in, deff_nm, rest_op]
    grompp_stage = 0

    grompp_input = inp_grompp(file_name, *input_list)
    make_index(file_name, run_type, coord_in)
    run_grompp(file_name, run_type, grompp_input, grompp_stage)




def eq1_run(run_type, top_in):
    coord_in = "en_min.gro"
    mdp_in = "premd1.mdp" 
    coord_in = "en_min.gro"
    mdp_in = "premd1.mdp" 
    deff_nm = mdp_in.split(".")[0] #naming scheme for the run used by gmx in next step
    tpr_input = deff_nm + ".tpr"
    rest_op = coord_in
    input_list = [coord_in, top_in, mdp_in, deff_nm, rest_op]
    grompp_stage = "eq"

    grompp_input = inp_grompp(file_name, *input_list)
    make_index(file_name, run_type, coord_in)
    run_grompp(file_name, run_type, grompp_input, grompp_stage)




def eq2_run(run_type, top_in):
    coord_in = "premd1.gro"
    mdp_in = "premd2.mdp" 
    deff_nm = mdp_in.split(".")[0] #naming scheme for the run used by gmx in next step
    tpr_input = deff_nm + ".tpr"
    rest_op = None
    input_list = [coord_in, top_in, mdp_in, deff_nm, rest_op]
    grompp_stage = True 

    grompp_input = inp_grompp(file_name, *input_list)
    make_index(file_name, run_type, coord_in)
    run_grompp(file_name, run_type, grompp_input, grompp_stage)




def prod295_run(run_type, top_in):
    coord_in = "premd2.gro"
    mdp_in = "md_295.mdp" 
    deff_nm = mdp_in.split(".")[0] #naming scheme for the run used by gmx in next step
    rest_op = None
    input_list = [coord_in, top_in, mdp_in, deff_nm, rest_op]
    grompp_stage = True

    grompp_input = inp_grompp(file_name, *input_list)
    make_index(file_name, run_type, coord_in)
    run_grompp(file_name, run_type, grompp_input, grompp_stage)




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


minimization_run(run_type, top_in)
run_mdrun(run_type, "en_min")
eq1_run(run_type, top_in)
run_mdrun(run_type, "premd1")
eq2_run(run_type, top_in)
run_mdrun(run_type, "premd2")
prod295_run(run_type, top_in)
run_mdrun(run_type, "md_295")
prod305_run(run_type, top_in)
run_mdrun(run_type, "md_305")



#grompp min1 L21
#inp_grompp

#mdrun min1 

#grompp eq1 min1_coord

#mdrun eq1

#grompp eq2 eq1_coord

#mdrun eq2

#grompp prod1 eq2_coord

#mdrun prod1

#grompp prod2 prod1_coord

#mdrun prod2

#analysis
