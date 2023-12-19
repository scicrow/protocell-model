#!/bin/bash -l
#SBATCH --account=pawsey0110
#SBATCH --job-name=md295_100nM_Na_Aqvist
#SBATCH --partition=work
#SBATCH --time=24:00:00
#SBATCH --ntasks=64
#SBATCH --ntasks-per-node=64
#SBATCH --cpus-per-task=1
#SBATCH --export=All

#======START=====
module load slurm
echo "The current job ID is $SLURM_JOB_ID"
echo "Running on $SLURM_JOB_NUM_NODES nodes"
echo "Using $SLURM_NTASKS_PER_NODE tasks per node"
echo "A total of $SLURM_NTASKS tasks is used"
echo "Node list:"
sacct --format=JobID,NodeList%100 -j $SLURM_JOB_ID

module load gromacs/2023

#These steps help slurm distribute jobs appropriately over cpus
export OMP_NUM_THREADS=1
export FI_CXI_DEFAULT_VNI=$(od -vAn -N4 -tu < /dev/urandom)

#This job will take approximately 36 hours to run but you can only request 24 hours
#at a time, so we'll need to submit this job so that the second job starts once the
#first is finished using resubmit.sh

#Remember to either run grompp step beforehand or uncomment it
gmx_mpi_d grompp -f md_295.mdp -c premd2.gro -p L21hybrid_bilayer_topol.top -n index.ndx -o md_295.tpr
srun -N $SLURM_JOB_NUM_NODES -n $SLURM_NTASKS -c $SLURM_CPUS_PER_TASK -m block:block:block gmx_mpi_d mdrun -dlb yes -deffnm md_295 -cpi -maxh 24.2
