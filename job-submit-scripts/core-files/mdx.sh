#!/bin/bash

time_stamp=$(date +%m-%d-%H-%M)
new_run=$time_stamp'_mdrun'
cur_dir=$(pwd)

run_dir='../'$new_run
mkdir $run_dir
cd $run_dir
cp -r $cur_dir $run_dir/. 
run_dir=$(pwd)
echo "$run_dir created and $cur_dir copied into it."
core_dir=$run_dir"/core-files"

echo "Running $core_dir/run_lib.py"
python3 $core_dir/run_lib.py "min" "gmx" $core_dir $run_dir
