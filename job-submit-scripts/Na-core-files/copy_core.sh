#!/bin/bash

time_stamp=$(date +%m-%d-%H-%M)
cur_dir=$(pwd)
echo $cur_dir
parent_dir="$(dirname "$cur_dir")"

#setting internal field separator to separate dir path
#IFS set means no forward slashes for directories
IFS='/'
read -ra dir_array <<< "$cur_dir"
dir_name="${dir_array[-1]}"
unset IFS


run_dir="$parent_dir/$time_stamp"'_NAions'

mkdir $run_dir
cd $run_dir
cp -r $cur_dir $run_dir/. 
run_dir=$(pwd)
echo "$run_dir created and $cur_dir copied into it."
core_dir=$run_dir"/"$dir_name

mv $core_dir"/mdx.sh" $run_dir
mv $core_dir"/runsbatch.sh" $run_dir
