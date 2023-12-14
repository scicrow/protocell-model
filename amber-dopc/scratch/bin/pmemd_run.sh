#!/bin/bash

naming_function() {
	# something like this but taking an input from pdb and using it to generate all the names for output files for later functions????
	in_name="$1"
	parm_file="${in_name}.prmtop"
	coord_file="$in_name.inpcrd"
	min_file="${in_name}_restrt.ncrst" # restart file for minimization. should probably link this to the function at some point and name it better
	heat_file="${in_name}_heat.ncrst"
	prod_traj="${in_name}_prod.nc"
	in_array=("$parm_file" "$coord_file" "$min_file" "$heat_file" "$prod_traj")
	echo "$in_array"
}
# script to run the minimization step with sander
run_minimization () {
	in_array=$@
	# -r is restart file from energy minimization
	echo "pmemd.MPI -O -i 01_min.in -o 01_min.out -p ${in_array[0]} -c ${in_array[1]} -r ${in_array[2]} -inf 01_min.mdinfo"
}

# script to run the heating step with sander
run_heating () {
	in_array=$@
	# -c needs to be restart file from minimization  -r is heating restart -x is output trajectory for MD. 
	echo	"pmemd.MPI -O -i 02_heat.in -o 02_heat.out -p ${in_array[0]} -c ${in_array[2]} -r ${in_array[3]} -x 02_heat.nc -inf 02_heat.mdinfo"
	echo "$parm_file, $min_file are your inputs"
	# -x is output trajectory -r is the restart file
}

# MD simulation script
run_prod () {
	in_array=$@  # needs the 02_heat.ncrst file as the coord

	echo "pmemd.MPI -O -v -i 03_prod.in -o 03_prod.out -p ${in_array[0]} -c ${in_array[3]} -r 03_prod.ncrst -x 03_prod.nc -inf 03_prod.info"
	echo "Completed. $parm_file and $heat_file are your inputs"
	# -x is output trajectory, r is restart file. 
}

check_name() {

}
in_array=$(naming_function "$@")
	[ -z "$file_name" ] && read -p "enter a file name..." FILENAME

echo $in_array
#run_minimization "$in_array"
#run_heating "$in_array"
#run_prod "$in_array"
