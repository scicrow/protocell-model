#!/bin/python
#
#Thomas Crow 2023
#functions that govern making and submitting sbatch jobs for MD. 

import subprocess
from datetime import datetime

def sbatch_jobname():  #needs job name input????
	#copies a template sbatch script, making a new one with new job name based on input and timestamp.  	

	sbatch_submit = "js_tom.sbatch"
	step_sub = "file_name"
	
	#timestamps the job
	now = datetime.now()
	sb_name = now.strftime("%y%m%d_%H%M")
	
	#creates new arguments for the sbatch job
	job_type = "test"
	change_jobname = "#SBATCH --job-name="
	job_name = job_type  + sb_name 
	sb_copy = sb_name + job_type + "_.sbatch"
	print (sb_copy)

	#would be nice to have error handling in here

	#create copy of template sbatch file
	subprocess.run(["cp", sbatch_submit, sb_copy])
		
	
	#modify the job specs in the copied file
	subprocess.run(["sed", "-i", 's/\\({}\\).*/\\1{}/'.format(change_jobname, job_name), sb_copy])
	# s/ subtitution
	# \({}\) capturing group in regular expression for change_jobname to replace \\ escape parentheses of regular expression
	# .*/ matches caracters .* until end of line
	# \1{} is rep[lacement part. 1 means only the first capturing group in the pattern
	
def sbatch_srun():
	#this will be the function that determines the type of srun job command to run. should probably also figure out dependency maybe?




sbatch_builder()

#sbatch_exe() {
	#runs the sbatch script developed by sbatch_builder
	#sbatch $filename
	#something like:
	#if:
	#jobid returns on 1, rerun jobid


#}


