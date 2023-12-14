#!/bin/bash

# This file needs to: 
# import the relevant things for python maybe? 
# 


dir_name="$HOME/simulation-$(date +%y-%m-%d-%H:%M)"

# mkdir $dir_name $amber_dir $gmx_dir

dir_check () {
	# this is a function for checking if a simulation directory exists and make a version for the simulation to run 
	i=$1
	vers_num=1
	new_dir=$i
	#echo "$i \n"
	while [ -d "$new_dir" ]; do
		if [ -d "$new_dir-run-$vers_num" ]; then
			while [ -d "$i-run-$vers_num" ]; do
				((vers_num++))
				new_dir="$i-run-$vers_num"
			done
		else
			new_dir="$i-run-$vers_num"
		fi

 
	done
	echo "$new_dir"
}

dir_out=$(dir_check "$dir_name")

echo "$dir_out"

# variables down here must have dir_out defined first (through dir_check to properly configure paths)
amber_dir="$dir_out/amber_simulation"
gmx_dir="$dir_out/gromacs_simulation"

mkdir $dir_out 
mkdir $amber_dir $gmx_dir
