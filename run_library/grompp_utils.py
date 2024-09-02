#!/bin/python

# Run by grompp_run.py, requires config.yaml in same directory

import os
import subprocess
import yaml


def configure_environment (path_script):
    #Loads local configuration file. Must exist in same directory.
    # Only have this run if global variable doesn't exist.

    try: 
        config_loc = str(f"{path_script}/config.yaml")
   
        with open(config_loc, "r", encoding="utf-8") as config_file:
            gromacs = yaml.load(config_file, Loader=yaml.FullLoader)
            print ("Loading local environment...\n"
                "Gromacs version is...", gromacs[0]['Local_environment']['gromacs_version'])
            gmx_command = str(gromacs[0]['Local_environment']['gromacs_command'])
            config_file.close()
    
    except:
        print(config_loc, "is missing! Where is your yaml file?")
        
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



def run_grompp(path_d, gmx_command, coor_in, temp_in, max_warn):
    # Needs a minimized run. Capable of premd and md runs.
    
    mdp_one = f"{path_d}/mdp/{temp_in}.mdp"
    coor_one = f"{path_d}/{coor_in}.gro"
    index_one = f"{path_d}/index.ndx"
    out_one = f"{path_d}/{temp_in}.tpr"
    top_in = f"{path_d}/topol.top"

    
    # Used to log missing files and quit function
    error_var = 0 
    # Check if all required files exist
    required_files = [mdp_one, coor_one, index_one, top_in]
    
    for file_path in required_files:
        if not os.path.exists(file_path):
            # Exit the script for missing files.
            print(f"Error: Required file '{file_path}' not found.")
            error_var = error_var + 1
            
    if error_var == 0:
        gromacs_run = [
        gmx_command, "grompp",
        "-f", mdp_one,
        "-c", coor_one,
        "-r", coor_one,
        "-n", index_one,
        "-o", out_one,
        "-p", top_in
        ]
        
        #print(gromacs_run)
        subprocess.run(gromacs_run, check = True)
    else:
        print("Grompp failed to complete. Check errors.")

        
    return()
