#!/bin/bash

dir=$(pwd) 
sbatch_loc="/home/tcrow/sbatch_commands/mdrun.sbatch"
run_var="$1" # eg. md_295 
num_runs=$2 # -1 for premd1, 0 for premd2, 3 for 200ns runs
job_name=$(basename "$dir") # saves the directory name as the job name
echo "Job name is: $job_name"
echo "Running $run_var with $num_runs additional runs."

submit_jobs () {
	#Submits first time and stores jobid
	jobid=$(sbatch --parsable $sbatch_loc $run_var $job_name)
	echo "Job ID is: $jobid"

	#Submits second time dependant on first job completing successfully
	#Wrap this in a for loop if you want a longer chain of dependancies



	counter=0
	while [ $counter -le $num_runs ] # 4 runs total
	do    
	    jobid=$(sbatch --parsable --dependency=afterok:$jobid $sbatch_loc $run_var $job_name)
	    echo "Dependent job is: $jobid"
	    ((counter++)) 
	done
}




#check if the file exists
#if [ -f $mdp ]; then
submit_jobs
#   #echo "File $mdp exists."
#else
#   echo "File $mdp does not exist."
#fi


