#!/bin/bash

time_stamp=$(date +%m-%d-%H-%M)
new_run=$time_stamp'_mdrun'
cur_dir=$(pwd)
echo $cur_dir
#setting internal field separator to separate dir path
IFS='/'
read -ra dir_array <<< "$cur_dir"

dir_name="${dir_array[-1]}"

run_dir='../'$new_run


mkdir $run_dir
cd $run_dir
cp -r $cur_dir $run_dir/. 
#run_dir=$(pwd)
#echo "$run_dir created and $cur_dir copied into it."
#core_dir=$run_dir"/"$dir_name

#mv $core_dir"/mdx.sh" $run_dir
#mv $core_dir"/runsbatch.sh" $run_dir
