# Thomas Crow
#analysis based on:
#Saeedimasine, M., Montanino, A., Kleiven, S. et al. 
#Role of lipid composition on the structural and mechanical features of axonal membranes: a molecular simulation study. 
#Sci Rep 9, 8000 (2019). https://doi.org/10.1038/s41598-019-44318-9
#
#APL, bilayer thickness, carbon order parameters, hydrogen bonds, number of lipid contacts, solvent accessible service, lipit interdigitation? and water permeability.
#
#
#The average APL was calculated by multiplying the x/y dimensions of pbc box and divide by number of decanoate/acid molecules present in one leaflet of the bilayer.
#
#Bilayer thickness calculated as distance between phospate peaks in the electron density profile (THIS IS FROM ORIGINAL PAPER. CHANGE THIS)

#import numpy as npo
import matplotlib.pyplot as plt
import subprocess

# need to read the xtc file and probably also need the gro file
# xtc is compressed, portable version of the trajectory file trr.
#gmx commands and index files are useful analysis tools
# note: in amber these would obviously be diferrent

# analysis of gromacs: https://manual.gromacs.org/current/reference-manual/analysis/using-groups.html



def debug_sub ():
	subprocess.run(["echo " + "Hello world"], shell=True, text=True)



def apl_function (): #(xy_coords, dec_num, steps);
	# every $steps, take the x-value and y-value and multiply them. Then divide by half the number of lipids (for a bilayer... 
	# assuming number of lipids in each bilayer is equal and none have flown off. This is a big guess, so I should probably count number of lipids at each timestep?
	subprocess.run(['gmx traj -f $xtc -ob box.xvg -s $tpr_gro -n $ndx -[yes]xyz '], shell=True, text=True) #trying to generate the xyz coords over time of the box
	# -ob = box xvg file
	# box_size = x * y
	# lipid_bilayer = dec_num / 2 # note: find a better way to calculate the lipids in the bilayer
	# area_per_lipid = box_size / lipid_ bilayer
	# return area_per_lipid
	
#function (stuff);
	#need to keep track of the conserved energy over time. possibly the total energy over time too. maybe the other stuff

#radial_distribution_function ();
	#do I need this? https://en.wikipedia.org/wiki/Radial_distribution_function
apl_function()
