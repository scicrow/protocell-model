#!/bin/bash

#	NOT paralellised, so I need to fix this from sander to sander x????

	PARM=dopc128x1_42w_lipid21.prmtop
	COORD=dopc128x1_42w_lipid21.inpcrd
	RESTRT=restrt.ncrst # restart file for minimization. should probably link this to the function at some point and name it better
	HEATF=02_heat.ncrst

# script to run the minimization step with sander
run_minimization () {
	local PARM_FILE=$1
	local COORD_FILE=$2
	# -r is minimization restart
	sander -O -i 01_min.in -o 01_min.out -p $PARM_FILE -c $COORD_FILE -r restrt.ncrst -inf 01_min.mdinfo
}

# script to run the heating step with sander
run_heating () {
	local PARM_FILE=$1
	local RES_FILE=$2
	# -c needs to be restart file from minimization  -r is heating restart -x is output trajectory for MD. 
	sander -O -i 02_heat.in -o 02_heat.out -p $PARM_FILE -c $RES_FILE -r 02_heat.ncrst -x 02_heat.nc -inf 02_heat.mdinfo
	echo "$PARM_FILE, $RES_FILE are your inputs"
}

# MD simulation script
run_prod () {
	local PARM_FILE=$1
	local HEAT_FILE=$2 # needs the 02_heat.ncrst file as the coord
	sander -O -v -i 03_prod.in -o 03_prod.out -p $PARM_FILE -c $HEAT_FILE -r 03_prod.ncrst -x 03_prod.nc -inf 03_prod.info
	echo "Completed. $PARM_FILE and $HEAT_FILE are your inputs"
}


# echo "what would you like to run?
# 	1 run minimization
# 	2 run heating
# 	3 run production"
# 
# read user_input
# 
# case $user_input in
# 	1)
# 	 echo "running minimization"
# 	 run_minimization $PARM $COORD
# 	 ;;
# 
# 	2)
# 	 echo "running heating"
# 	 run_heating $PARM $RESTRT
# 	 ;;
# 
# 	3)
# 	 echo "running production"
# 	 run_prod $PARM $HEATF
# 	 ;;
# 
# esac	
