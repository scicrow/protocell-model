#!/bin/bash

#module load gromacs/2023

run_dir=$(pwd)
core_dir=$run_dir"/K-core-files"
run_type=$@


echo "Running $core_dir/run_lib.py"
python3 $core_dir/run_lib.py $run_type "gmx" $core_dir $run_dir