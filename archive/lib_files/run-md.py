#!/bin/python
# just random run testing commands

# gmx_mpi is parallelised. d specifies double precision. we actually want mixed precision but setonix doesn't have that installed.
#run_type = "srun gmx_mpi_d"
#debug_run()
#gromp_in = (inp_grompp(file_name, "mdp, coord, top, tpr, rstrt, index"))
#print (gromp_in)
#run_grompp(file_name, gromp_in)
#run_mdrun(file_name, "test")

# a bash command will input certain parameters, then this python script will
# take the inputs, and use lib-md.py functions to run gromacs.

try:
	import lib_md as lib
except Exception as e:
	print(f"lib-md.py failed to load! Make sure it is in the same directory as run-md.py")

run_type = "mdp_gmx"

#def run_in ():
	#might already have this?


def grompp_in (lib_name, run_type, input_list):
	#print (input_list)	
	inp_args = input_list[1:]
	min_args = lib.inp_grompp(lib_name, inp_args) #needs 2 args
	lib.run_grompp(lib_name, run_type, min_args) #needs 3 args

def min1_run(min_list):
	#keep this separate so can be recalled if timing out.
	lib.run_mdrun(*min_list)
	

def eq1_run(eq1_list): #same or different list?
	lib.run_mdrun(*eq1_list)


def eq2_run(eq2_list): #same or different list?
	lib.run_mdrun(eq2_list)


def prod1_run(prod1_list): #same or different list?
	lib.run_mdrun(prod1_list)


def prod2_run(prod2_list): #same or different list?
	lib.run_mdrun(prod2_list)

#okay, but how is this function going to repeat if it isn't finished????


test_list = ["runtype", "coord", "topology", "something", "somethingelse"]
#grompp_in(lib, run_type, test_list)
min1_run(test_list)

#class for each??
	 
#minimization 1:
#checkname funciton
#grompp function
#mdx function
#chekpoint function
#if command == 0 move on to minimization 2

#minimization 2:
#checkname function
#grompp
#mdx
#checkpoint

#bash script will then prep equilibration 

#equilibration 1:
#checkname
#grompp
#mdx
#checkpoint
#if command == 0 move on to equilibration 2:

#equilibration 2:
#checkname
#grompp
#mdx
#checkpoint


#bash script will then prep prod

#prod1

#prod2

