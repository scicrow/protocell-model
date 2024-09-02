#!/bin/python

import os
import argparse
from grompp_utils import * 

# Receive arguments
parser = argparse.ArgumentParser(description='Receive gromacs inputs')

parser.add_argument('temp_in', type=str, 
                    help='Specify the run temperature. Examples: premd1 premd2 md_295 md_305... md_375')
parser.add_argument('coor_in', type=str, help='Include coordinate file. Expected .gro or .pdb')

parser.add_argument('-mw', '--maxwarn', default=0, type=int,
                    help='Increase maxwarn. Useful for gen-vel. Default=0')

args = parser.parse_args()
#print("arguments are... ", args)



path_d = os.getcwd()
path_script = os.path.dirname(os.path.abspath(__file__))
#print(path_d)
#print(path_script)


coor_in = args.coor_in
temp_in = args.temp_in
max_warn = args.maxwarn

gmx_command = configure_environment(path_script) 
run_grompp(path_d, gmx_command, coor_in, temp_in, max_warn)