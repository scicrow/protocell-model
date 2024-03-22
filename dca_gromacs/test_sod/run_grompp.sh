#!/bin/bash
path_d=$(pwd)
mdp_in=$path_d"/mdp/en_min.mdp"
coor_in=$path_d"/deca_100mm_nacl.pdb"
out_in=$path_d"/min.tpr"
top_in=$path_d"/topol.top"
deff_nm="min"

#gmx grompp -f $mdp_in -c $coor_in -o $out_in -p $top_in
#gmx mdrun -cpi -maxh 24.2 -deffnm $deff_nm


#second minimization run
mdp_two=$path_d"/mdp/en_min2.mdp"
coor_two=$path_d"/min.gro"
out_two=$path_d"/min2.tpr"
deff_nm="min2"

#gmx grompp -f $mdp_two -c $coor_two -o $out_two -p $top_in
#gmx mdrun -cpi -maxh 24.2 -deffnm $deff_nm

mdp_premd=$path_d"/mdp/premd1.mdp"
coor_premd=$path_d"/min2.gro"
out_premd=$path_d"/premd.tpr"
deff_nm="premd"
#gmx grompp -f $mdp_premd -c $coor_premd -r $coor_premd -n index.ndx -o $out_premd -p topol.top
#gmx mdrun -cpi -maxh 24.2 -deffnm $deff_nm


mdp_premd=$path_d"/mdp/premd2.mdp"
coor_premd=$path_d"/premd.gro"
out_premd=$path_d"/premd2.tpr"
deff_nm="premd2"
gmx grompp -f $mdp_premd -c $coor_premd -r $coor_premd -n index.ndx -o $out_premd -p topol.top
gmx mdrun -cpi -maxh 24.2 -deffnm $deff_nm
