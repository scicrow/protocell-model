#!/bin/bash
# Thomas Crow 2023
# based on resubmit.sh, written by Cara 
#

job_submit=""
job_id=""




sbatch_builder() { #needs job name input????
	#copies a template sbatch script, making a new one with new job name based on input and timestamp.  	

	#cl_input=$@	#maybe some error handling here to make sure you have good inputs
	sbatch_submit="js_tom.sbatch"
	step_sub="file_name"
	change_jobname="#SBATCH --job-name="
	sb_name="$(date +"%Y%b%d_%H%M")"
	sb_copy=$sb_name"_.sbatch"
	cp "$sbatch_submit" "$sb_copy"
	
	sed -i 's/\('"$change_jobname"'\).*/\1'"$sb_name"'/' "$sb_copy"
	echo $sb_copy
	#might also need to sed change the command based on the filename
}

sbatch_exe() {
	#runs the sbatch script developed by sbatch_builder
	#sbatch $filename
	#something like:
	#if:
	#jobid returns on 1, rerun jobid


}






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
