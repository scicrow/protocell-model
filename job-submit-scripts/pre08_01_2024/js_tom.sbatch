#!/bin/bash -l
#SBATCH --account=pawsey0110
#SBATCH --job-name=
#SBATCH --partition=work
#SBATCH --time=024:00:00
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

#srungoeshere

#this was the original script
#srun -N $SLURM_JOB_NUM_NODES -n $SLURM_NTASKS -c $SLURM_CPUS_PER_TASK -m block:block:block python run-md.py $input #gmx_mpi_d mdrun $run_func
