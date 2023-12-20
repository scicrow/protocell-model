# just random run testing commands

# gmx_mpi is parallelised. d specifies double precision. we actually want mixed precision but setonix doesn't have that installed.
run_type = "srun gmx_mpi_d"
#debug_run()
#gromp_in = (inp_grompp(file_name, "mdp, coord, top, tpr, rstrt, index"))
#print (gromp_in)
#run_grompp(file_name, gromp_in)
#run_mdrun(file_name, "test")


