#!/bin/bash



#copy into your md run directory for running analysis. directories and commands assume Setonix setup
#written for gromacs\2024 https://manual.gromacs.org/current/onlinehelp/gmx-density.html
#requires input arguments arg1=md temp prefix, arg2 = title you want for your graphs eg. "C14 acid in 100 mM KCl at 295 K"

dir=(pwd)
an_dir=$MYSCRATCH/analysis_scripts/
title=$2

#gmx traj -s premd2.gro -n index.ndx -f md_295.xtc -z -y -x -ob md295_box

input_checker () {
    #checks input and determines what kind of analysis user wants to do
	case $1 in 
	
    	md_295)
	        echo "running analysis of md_295 files"
			gro_in=$(dir)premd2.gro
			xtc_in=$(dir)md_295.xtc
			tpr_in=$(dir)md_295.tpr
			ob_out=$(dir)traj_295
			dens_out=$(dir)dens_295
		    ;;
	    md_305)
	        echo "running analysis of md_305 files"
			gro_in=$(dir)md_295.gro
			xtc_in=$(dir)traj_305
			tpr_in=$(dir)md_305.tpr
			ob_out=$(dir)traj_305
			dens_out=$(dir)dens_305
		    ;;
		md_315)
	        echo "running analysis of md_315 files"
			gro_in=$(dir)md305.gro
			xtc_in=$(dir)traj_315
			tpr_in=$(dir)md_315.tpr
			ob_out=$(dir)traj_315
			dens_out=$(dir)dens_315
		    ;;	
		md_325)
	        echo "running analysis of md_325 files"
			gro_in=$(dir)md315.gro
			xtc_in=$(dir)traj_325
			tpr_in=$(dir)md_325.tpr
			ob_out=$(dir)traj_325
			dens_out=$(dir)dens_325
		    ;;	
		md_335)
	        echo "running analysis of md_335 files"
			gro_in=$(dir)md325.gro
			xtc_in=$(dir)traj_335
			tpr_in=$(dir)md_335.tpr
			ob_out=$(dir)traj_335
			dens_out=$(dir)dens_335
		    ;;	
	    md_345)
	        echo "running analysis of md_345 files"
			gro_in=$(dir)md335.gro
			xtc_in=$(dir)traj_345
			tpr_in=$(dir)md_345.tpr
			ob_out=$(dir)traj_345
			dens_out=$(dir)dens_345
		    ;;		
	    *)
	        echo "unknown input"
            ;;
	esac


    #if [ -f $gro_in ];
	#check if the files in each variable are present or else force quit this shell and display an error
	
#generates box size at each time to determine area per lipid (only concerned with x-y area)
#if not using on setonix, gmx_mpi must be changed to gmx
gmx_mpi traj -s $gro_in -n index.ndx -f $xtc_in -z -y -x -ob $ob_out #gets box vectors at each time step for apl. use -oc if you want coords

#run gmx density to get density of 4 groups, TIP3p, POT, CLA and MYR_MYRP.
echo "7\n 6\n 5\n 4\n"| gmx_mpi density -f $xtc_in -n index.ndx -s $tpr_in -ng 4 -sl 500 -o $dens_out


}

run_analysis () {
    #run APL analysis requires arg1 = xvg filename, arg2 = title
    python "${an_dir}apl_analysis.py" "${ob_out}.xvg" "Area per lipid of ${title}"
	
	

}


input_checker $1
run_analysis