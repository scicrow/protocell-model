#!/bin/bash

# Thomas Crow - 2024

#copy into your md run directory for running analysis. directories and commands assume Setonix setup
#written for gromacs\2024 https://manual.gromacs.org/current/onlinehelp/gmx-density.html


directory_path=$(pwd)
analysis_directory=$(pwd)
parent_directory=$(basename "$directory_path")


# A dictionary (associative array) that stores .xtc names and pulls the corresponding .gro filename


declare -A traj_dict
traj_dict=(
	["md_295.xtc"]="premd2.gro"
	["md_305.xtc"]="md_295.gro"
	["md_315.xtc"]="md_305.gro"
	["md_325.xtc"]="md_315.gro"
	["md_335.xtc"]="md_325.gro"
	["md_345.xtc"]="md_335.gro"
	["md_355.xtc"]="md_345.gro"
)






#find all .xtc (trajectory) files and adds them to an array 
xtc_files=()
while IFS=  read -r -d $'\0'; do
    xtc_files+=("$REPLY")
done < <(find "$directory_path" -type f -name "*.xtc" -print0)




# Check the trajectory dictionary for corresponding coordinate filenames and save them to an array
coord_array=()
tpr_array=()
density_array=()
title_array=()


for traj in "${xtc_files[@]}"; do
    traj_name=$(basename "$traj")
    #echo $traj_name
    if [[ -v traj_dict["$traj_name"] ]]; then
       coord=${traj_dict["$traj_name"]}
       tpr_in="${traj%.???}.tpr"
       density_out="${traj%.???}"
       
       # Formatting for Matplotlib chart
       temp_title=$(basename ${tpr_in%.???})
       temp_title="${temp_title:3}"
       apl_title="APL of $parent_directory at $temp_title K"

       echo "Trajectory: $traj_name, Value: $coord, Run Input: $tpr_in, Density output: $density_out"
       coord_array+=("$directory_path"/"$coord")
       tpr_array+=("$tpr_in")
       density_array+=("$density_out")
       echo "
       apl_title is:$apl_title

       "
       title_array+=("$apl_title")
    else
     echo "File $traj_name has no corresponding coordinate file"
    fi     

done





# Write the box size of each run to determine apl (only concerned with x-y box size).
# Then make a chart. Change the apl_analysis variable if using a different script
apl_analysis="apl_analysis.py"
count=0
while [ $count -lt ${#coord_array[@]} ]; do
        
	# Write the trajectory file (.xvg) and make sure Gromacs is installed
	echo "7" | gmx_mpi traj -s ${coord_array[$count]} -n index.ndx -f ${xtc_files[$count]} -z -y -x -ob ${density_array[$count]}
        
	gmx_status=$?

        if [ $gmx_status -ne 0 ]; then
            echo "Error: gmx_mpi command failed with exit code $gmx_status"
            exit $gmx_status
        fi	
	
	
	
	python "$apl_analysis" "${density_array[$count]}" "${title_array[$count]}"	
        python_status=$?
        if [ $python_status -ne 0 ]; then
            echo "Error: Python script failed with exit code $python_status"
            exit $python_status
        fi



done



