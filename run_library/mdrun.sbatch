#!/bin/bash -l

#SBATCH --account=pawsey0110-gpu
#SBATCH --partition=gpu
#SBATCH --time=24:00:00
#SBATCH --nodes=1
#SBATCH --export=All
#SBATCH --gres=gpu:1

nm_run=$1
job_name=$2

#echo "deff nm is $nm_run"

#======START=====
module load slurm
module unload cray-libsci
module load rocm/5.7.3
module load gromacs-amd-gfx90a/2023


echo "The current job ID is $SLURM_JOB_ID"
echo "Running on $SLURM_JOB_NUM_NODES nodes"
echo "Using $SLURM_NTASKS_PER_NODE tasks per node"
echo "A total of $SLURM_NTASKS tasks is used"
echo "Node list:"
sacct --format=JobID,NodeList%100 -j $SLURM_JOB_ID

#These steps help slurm distribute jobs appropriately over cpus
export OMP_NUM_THREADS=7
export FI_CXI_DEFAULT_VNI=$(od -vAn -N4 -tu < /dev/urandom)

srun -N $SLURM_JOB_NUM_NODES -N 1 -n 1 -c 8 --job-name=$job_name gmx_mpi mdrun -deffnm $nm_run -nb gpu -cpi -maxh 24.2
