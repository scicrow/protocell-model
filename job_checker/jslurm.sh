#!/bin/bash

scratch_dir="/scratch/pawsey0110/tcrow/"
work_dir="${scratch_dir}job_checker/"

save_dog() {
    #SAVE ALL RUNNING, SUSPENDED AND QUEUED JOBS IN LOG
	sacct -u tcrow --format=JobID,JobName,State --state=RUNNING,PENDING,SUSPENDED | tail -n +3 > ${work_dir}upsacct.log
	squeue -u tcrow -O "jobid,dependency" | tail -n +2 >> ${work_dir}upsacct.log
}




directory_check() {
	# SAVE SCRATCH SUB-DIRECTORIES IF THEY MENTION KCL (SIMULATIONS)
	shopt -s nullglob  # Ensures that the array is empty if no files are found
	dir_path=(${scratch_dir}*kcl*/)
	> ${work_dir}jobhis.log
	if [ ${#dir_path[@]} -eq 0 ]; then
		echo "No subdirectories found in directory path. Check path."
		exit 1	
	fi
	
	for d in "${dir_path[@]}"; do
		slurm_path=("${d}"slurm-*.out)
		for slurm in "${slurm_path[@]}"; do	
			slurm_basename=$(basename $slurm)
			slurm_id=$(echo "${slurm_basename}" | grep -o '[0-9]\+')
			dir_sl=$(basename $d)
			echo "${slurm_id} ${dir_sl}" >> ${work_dir}jobhis.log
			
		done
	done
	
	

	

}

#save_dog
directory_check
