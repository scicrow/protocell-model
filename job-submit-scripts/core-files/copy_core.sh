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

mv $core_dir"/mdx.sh" $run_dir
mv $core_dir"/runsbatch.sh" $run_dir
