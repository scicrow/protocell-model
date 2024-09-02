#!/bin/python

# commands to run this script: . run_grompp.sh; test_run teststring

import os
import subprocess
import yaml
import argparse

# Load some modules from the bash script

path_d = os.getcwd()
print(path_d)

coor_path = f"{path_d}/{coor_in}"
temp_in = [] #examples: premd1 premd2 md_295 md_305... md_375


parser = argparse.ArgumentParser(description='Receive gromacs inputs')
parser.add_argument('-c', help='Include coordinate file. Expected .gro or .pdb')
args = parser.parse_args()
coor_in = args.c

parser.add_argument('-t', help='Specify the run temperature. Examples: premd1 premd2 md_295 md_305... md_375')
args = parser.parse_args()
temp_in = args.t




def configure_environment ():
    #Loads local configuration file. Must exist in same directory.
    # Only have this run if global variable doesn't exist.
    with open("./config.yaml", "r", encoding="utf-8") as config_file:
        gromacs = yaml.safe_load(config_file, Loader=yaml.FullLoader)
        print ("Loading local environment...\n"
               "Gromacs version is...", gromacs[0]['Local_environment']['gromacs_version'])
        gmx_command = str(gromacs[0]['Local_environment']['gromacs_command'])
        config_file.close()
    
    #print ("Gromacs run command is... ", gromacs[0]['Local_environment']['gromacs_command'])
    #print ("Gromacs command is", gmx_command)
    return(gmx_command)



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
def run_grompp(path_d, gmx_command):

    #needs minimizations completed
    mdp_one = f"{path_d}/mdp/{temp_in}.mdp"
    coor_one = f"{path_d}/{temp_in}.gro"
    index_one = f"{path_d}/index.ndx"
    out_one = f"{path_d}/{temp_in}.tpr"
    top_in = f"{path_d}/topol.top"
    
    # used to log missing files and quit function
    error_var = 0 

    required_files = [mdp_one, coor_one, top_in, index_one, top_in]

# Check if all required files exist
    for file_path in required_files:
        if not os.path.exists(file_path):
            # Exit the script with an error code
            print(f"Error: Required file '{file_path}' not found.")
            error_var = error_var + 1
            
    if error_var == 0:
        gromacs_run = f"{gmx_command} grompp -f {mdp_one} -c {coor_one}"
        "-r {coor_one} -n {index_one} -o {out_one} -p {top_in}"
        print(gromacs_run)
        #subprocess.run(gromacs_run, check = True)
    else:
        print("Grompp failed to complete. Check errors.")
    
    #subprocess.run([gromacs, 'grompp',
    #'-f', mdp_one,  
    #'-c', coor_one, 
    #'-r', coor_one,
    #'-n', index_one,
    #'-o', out_one, 
    #'-p', top_in
    #], check = True)

        
    return()
    
run_grompp(path_d, "gmx")


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