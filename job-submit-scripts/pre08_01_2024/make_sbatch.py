#!/bin/python
#
#Thomas Crow 2023
#functions that govern making and submitting sbatch jobs for MD. 

import subprocess
from datetime import datetime

def sbatch_copy(): #inputs = job_type
	#copies a template sbatch script, making a new one with new job name based on input and timestamp.  	
	sbatch_submit = "js_tom.sbatch"
	
	#timestamps the job
	now = datetime.now()
	sb_name = now.strftime("%y%m%d_%H%M")

	job_type = "test"
	job_name = job_type  + sb_name 
	sb_copy = sb_name + job_type + "_.sbatch"


	#create copy of template sbatch file
	try:
		subprocess.run(["cp", sbatch_submit, sb_copy])

	except Exception as e:
		print("Error with sbatch_copy function. check your inputs are correct. Error is: ", e)
 
	#return variables that are needed for sbatch_jobname and sbatch_srun
	return (job_name, sb_copy) #might want to use iterative unpacking for any instance of calling this function 




def sbatch_jobname(job_name, sb_copy):  
	
	change_jobname = "#SBATCH --job-name="

	#modify the job specs in the copied file
	subprocess.run(["sed", "-i", 's/\\({}\\).*/\\1{}/'.format(change_jobname, job_name), sb_copy])
	# s/ subtitution
	# \({}\) capturing group in regular expression for change_jobname to replace \\ escape parentheses of regular expression
	# .*/ matches caracters .* until end of line
	# \1{} is rep[lacement part. 1 means only the first capturing group in the pattern




def sbatch_srun(sb_copy):
	#this will be the function that determines the type of srun job command to run. should probably also figure out dependency maybe?
	replace_line = '#srungoeshere'
	new_line = 'replacementline'
	
	subprocess.run(["sed", "-i", 's/{}/{}/'.format(replace_line, new_line), sb_copy])
	#check sbatch_jobname for documentation on how this command works.
	#important difference is it replaces the hole line with the new_line variable.


job_name, sb_copy = sbatch_copy()
sbatch_jobname(job_name, sb_copy)
sbatch_srun(sb_copy)

#sbatch_exe() {


#}


