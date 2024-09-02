#!/bin/python

# commands to run this script: . run_grompp.sh; test_run teststring 
# this will run this script, run the test_run function and have the working directory as $1 and teststring as input $2

import os
import subprocess

# Load some modules from the bash script

path_d = os.getcwd()
print(path_d)
top_in = f"{path_d}/topol.top"
coor_in = [] # coord argument in 
coor_path = f"{path_d}/{coor_in}"
temp_in = [] #examples: premd1 premd2 md_295 md_305... md_375

gromacs = "gmx_mpi/gmx" #fix this to recognise native gromacs

#def min():
#    #first minimization run 
#    mdp_in=$path_d"/mdp/en_min.mdp"
#    coor_one=$path_d"/$coord"
#    out_one=$path_d"/min.tpr"
#    top_in=$path_d"/topol.top"
#    deff_nm="min"
#    gmx_mpi grompp -f $mdp_in -c $coor_one -o $out_one -p $top_in
#    gmx_mpi mdrun -cpi -maxh 24.2 -deffnm $deff_nm
#    
#    #second minimization run
#    mdp_two=$path_d"/mdp/en_min2.mdp"
#    coor_two=$path_d"/min.gro"
#    out_two=$path_d"/min2.tpr"
#    deff_nm="min2"
#    gmx_mpi grompp -f $mdp_two -c $coor_two -o $out_two -p $top_in
#    gmx_mpi mdrun -cpi -maxh 24.2 -deffnm $deff_nm
#
#    return()
#
def run_grompp(path_d):
#
#    
    #needs minimizations completed
    try: 
    
        mdp_one = f"{path_d}/mdp/{temp_in}.mdp"
        coor_one = f"{path_d}/{temp_in}.gro"
        index_one = f"{path_d}/index.ndx"
        out_one = f"{path_d}/{temp_in}.tpr"
	
	
    #    input_list=[$mdp_one, $coor_one, $top_in, $index_one]
	
	
        subprocess.run([gromacs, 'grompp',
        '-f', mdp_one,  
        '-c', coor_one, 
        '-r', coor_one,
        '-n', index_one,
        '-o', out_one, 
        '-p', top_in
        ], check = True)
        
    except Exception as e:
        print("Failed due to error(s): \n", e)
        
    return()
    
run_grompp(path_d)


#def file_checker (file_in):
#	os.path.isfile(file_in)
#    
#    if [ -f $FILE ]; then
#       echo "File $FILE exists."
#    else
#       echo "File $FILE does not exist."
#    fi
#
#    return()
#
#
#test_run() {
#    echo "input 1 is $1"
#    echo "input 2 is $2"
#    echo "input 3 is $3"
#}