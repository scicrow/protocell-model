#/bin/python
#
#Thomas Crow 2023
#functions that govern making and submitting sbatch jobs for MD. 

import sys
import subprocess
from datetime import datetime
subprocess.run("module load gromacs/2023", shell = True)

#filled by input_checker function. while None, the other functions won't run 
job_type = None


def sbatch_copy(job_type, run_dir, core_dir): #inputs = job_type
	#copies a template sbatch script, making a new one with new job name based on input and timestamp.	
	sbatch_submit = core_dir + "/sbatch_template"
	
	job_name = job_type
	sb_copy = job_type + ".sbatch" #sbatch job name
	sb_location = run_dir + "/" + sb_copy # location should be in run directory

	#create copy of template sbatch file
	try:
		subprocess.run(["cp", sbatch_submit, sb_location])

	except Exception as e:
		print("Error with sbatch_copy function. check your inputs are correct. Error is: ", e)
 
	#return variables that are needed for sbatch_jobname and sbatch_srun
	return (job_name, sb_location)




def sbatch_jobname(job_name, sb_loc):	
    #changes the job name in the new sbatch script (sb_copy)

	change_jobname = "#SBATCH --job-name="

	#modify the job specs in the copied file
	subprocess.run(["sed", "-i", 's/\\({}\\).*/\\1{}/'.format(change_jobname, job_name), sb_loc])
	# s/ subtitution
	# \({}\) capturing group in regular expression for change_jobname to replace \\ escape parentheses of regular expression
	# .*/ matches caracters .* until end of line
	# \1{} is rep[lacement part. 1 means only the first capturing group in the pattern




def sbatch_type(sb_loc, sbatch_input):
	#adds the command to run run_md.py as a slurm job. needs to know the job type and the new sbatch script (sb_copy)
    replace_line = "srun -N $SLURM_JOB_NUM_NODES -n $SLURM_NTASKS -c $SLURM_CPUS_PER_TASK -m block:block:block "

    subprocess.run(["sed", "-i", 's/\\({}\\).*/\\1{}/'.format(replace_line, sbatch_input), sb_loc])
	#check sbatch_jobname for documentation on how this command works.
	#important difference is it replaces the hole line with the new_line variable.




def run_sbatch(job_type):
    #unfinished
    job_name = job_type + ".sbatch"
    depend_job = "--dependency=afterok:" + job_name
    #subprocess.run(['sbatch', '--parsable', job_name])
    print (depend_job)
    print ("job name is : " + job_name)



def input_checker(run_type):
    #checks you are specifying a simulation type that run_lib.py can understand.
    run_list = ['min', 'eq1', 'eq2', '295', '305']
    run_type = str(run_type).lower()
    if run_type in run_list:
       # print ("command is correct")
       return run_type
    else:
         print ("command not found!")
    

#Submits first time and stores jobid
#jobid=$(sbatch --parsable job_submit_md295.sh --dependency=afterok:6088167)

#Submits second time dependant on first job completing successfully
#Wrap this in a for loop if you want a longer chain of dependancies
#jobid=$(sbatch --parsable job_submit_md295.sh --dependency=afterok:$jobid)


