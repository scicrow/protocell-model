#Submits first time and stores jobid
jobid=$(sbatch --parsable job_submit_md295.sh --dependency=afterok:6088167| cut -d " " -f 4)

#Submits second time dependant on first job completing successfully
#Wrap this in a for loop if you want a longer chain of dependancies
jobid=$(sbatch --parsable job_submit_md295.sh --dependency=afterok:$jobid | cut -d " " -f 4)
