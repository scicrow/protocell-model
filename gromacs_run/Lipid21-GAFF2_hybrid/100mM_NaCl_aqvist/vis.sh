#When you want to visualise a trajectory in vmd, you need  to do some preparation on it
#first to make the molecules appear whole:
gmx_mpi_d trjconv -f premd1.xtc -s premd1.tpr -o premd1_vis.xtc -pbc whole
gmx_mpi_d trjconv -f premd2.xtc -s premd2.tpr -o premd2_vis.xtc -pbc whole

#If you want to visualise on Setonix instead of transferring the file locally, use the
#visualisation portal at:
#https://vis.pawsey.org.au/remotevis/#/
#and follow these instructions:
#https://support.pawsey.org.au/documentation/display/US/VMD+on+Setonix+Remote+Visualisation
#You might need to request access for your account through help@pawsey.org.au first
