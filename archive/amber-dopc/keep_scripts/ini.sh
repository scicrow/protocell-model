#!/bin/bash

# read -p "What's the pdb file?" pdb_input
# some error checking if you have more than one file. may not be strictly necessary?

pdb_in="*.pdb"

#echo $pdb_in
source run-gmx.sh

# run_gmx "$pdb_in"

# run_acpype "$pdb_in"

check_leap "Hi"
