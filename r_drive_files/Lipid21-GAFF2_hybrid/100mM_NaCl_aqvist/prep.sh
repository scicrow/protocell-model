#These steps I would run either on WSL or directly in the terminal on Setonix
#Create index file
(echo 'r DCN'; echo 'r DCA | r DCN'; echo 'r SOL | r Na | r Cl'; echo 'name 10 Water_and_ions'; echo q) | gmx make_ndx -f L21hybrid_bilayer_100mM.pdb -o index.ndx

#Energy minimisation in 2 steps
gmx grompp -f en_min.mdp -c L21hybrid_bilayer_100mM.pdb -p L21hybrid_bilayer_topol.top -o en_min.tpr
gmx mdrun -deffnm en_min
gmx grompp -f en_min2.mdp -c en_min.gro -p L21hybrid_bilayer_topol.top -o en_min2.tpr
gmx mdrun -deffnm en_min2

#Grompp for initial equilibration period but don't run yet
gmx grompp -f premd1.mdp -c en_min2.gro -r en_min2.gro -p L21hybrid_bilayer_topol.top -n index.ndx -o premd1.tpr
#Remaining steps need to be submitted to queueing system