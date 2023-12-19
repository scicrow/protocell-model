# Thomas Crow 2023
# based on resubmit.sh, written by Cara 
#

job_submit=""
job_id="@"

#Submits first time and stores jobid
job_id=$(sbatch --parsable $job_submit --dependency=afterok:$job_id)




#old code from Cara --tom
#Submits second time dependant on first job completing successfully
#Wrap this in a for loop if you want a longer chain of dependancies
#jobid=$(sbatch --parsable job_submit_md295.sh --dependency=afterok:$jobid | cut -d " " -f 4)
