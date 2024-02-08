#!/bin/bash

module load gromacs/2023
module unload cray-libsci
module load openblas/0.3.21

run_dir=$(pwd)
core_dir=$run_dir"/Na-core-files"
run_type=$@


echo "Running $core_dir/run_lib.py"
python3 $core_dir/run_lib.py $run_type "gmx_mpi_d" $core_dir $run_dir
