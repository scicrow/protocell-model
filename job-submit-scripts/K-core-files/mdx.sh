#!/bin/bash

module load gromacs/2023

run_dir=$(pwd)
core_dir=$run_dir"/K-core-files"

echo "Running $core_dir/run_lib.py"
python3 $core_dir/run_lib.py "min" "gmx_mpi_d" $core_dir $run_dir
