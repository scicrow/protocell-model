#!/bin/bash
# Thomas Crow 2023
# based on resubmit.sh, written by Cara 
#

job_submit="min_eq_prod"
job_id=""

# run a minimization
# ru






#keep track of outputs
#probably make directories


#govern resubmit of sbatch -- how do you check that something's done? 



}

#Submits first time and stores jobid
#jobid=$(sbatch --parsable job_submit_md295.sh --dependency=afterok:6088167| cut -d " " -f 4)

#Submits second time dependant on first job completing successfully
#Wrap this in a for loop if you want a longer chain of dependancies
#jobid=$(sbatch --parsable job_submit_md295.sh --dependency=afterok:$jobid | cut -d " " -f 4)




#old code from Cara --tom
#Submits second time dependant on first job completing successfully
#Wrap this in a for loop if you want a longer chain of dependancies
#jobid=$(sbatch --parsable job_submit_md295.sh --dependency=afterok:$jobid | cut -d " " -f 4)
