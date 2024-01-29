#!/bin/bash

#run_dir=$(pwd)

#Submits first time and stores jobid
premd1=$(sbatch --parsable premd1.sbatch)

#Submits second time dependant on first job completing successfully
#Wrap this in a for loop if you want a longer chain of dependancies
#premd1=$(sbatch --parsable premd1.sbatch --dependency=afterok:$premd1)

#runs grompp and makes sbatch
#prep_premd2=$(sbatch --parsable  --dependency=afterok:$premd1)


#premd2=$(sbatch --parsable premd2.sbatch --dependency=afterok:$prep_premd2)

#premd2=$(sbatch --parsable premd2.sbatch --dependency=afterok:$premd2
