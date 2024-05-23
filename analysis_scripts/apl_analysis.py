#!/bin/python
# Thomas Crow

import numpy as np
import matplotlib.pyplot as plt
import sys

xvg = "295traj_myr.xvg"

def xvg_read(xvg):
    #reads a gromacs trajectory xvg file and removes the comments and starting blurb to the file
    with open(xvg, 'r') as f:
        out_read = f.readlines()
        clean_xvg = []
        start_line = False
        for line in out_read:
            if start_line != True and line[0] != "@" and line[0] != "#":
                start_line = True 
                #print(line)
            if start_line == True:
                clean_xvg.append(line.strip().split())
            
        #print(clean_xvg)

    return (clean_xvg)

def apl_function (clean_xvg):
    time = []
    apl_list = []
    for line in clean_xvg:
        time_string = float(line[0])
        time_string = time_string / 1000 # picoseconds to nanoseconds
        time.append(time_string)
        x_length = (line[1])
        x_length = float(x_length)
        xy_plane = x_length ** 2
        #assumes 144 lipids per layer
        apl = xy_plane / 144
        apl_list.append(apl)
       
    time = time[1::1]  
    apl_list = apl_list[1::1] #you'll have something like 2001 steps, you need even number for splitting so remove t=0
    apl_list = np.array(apl_list) #needed for array splitting
    time_average = time[0::500] #makes a time marker for each nanosecond
    
    #get the average apl at each nanosecond
    apl_average = [] 
    length_apl = len(apl_list)/500 
    print ("length of apl list is:", len(apl_list))
    print ("length_apl is", length_apl)
    length_apl = round(length_apl)
    print ("rounded length_apl is", length_apl)
    subarray_apl = np.split(apl_list, length_apl)
    #print (subarray_apl)
    
    #average over each nanosecond 
    for sub in subarray_apl:
        av_apl = sum(sub)/len(sub)
        print (av_apl)
        apl_average.append(av_apl)
        #print (apl_average)

    #print (apl_average)
    #print(time_average)
    #print("time is\n", time)
    #print("area per lipid is\n", apl_list)
    return(time, apl_list, time_average, apl_average)
    

def traj_pyplot(time, apl_list, xvg, time_average, apl_average):
    title = xvg.strip(".xvg")
    figure_file = title + ".png"
    title = "Mass density profile of C14 acid in 100 mM KCl @ 295 K"
    
    area_per_lipid =  plt.plot(time, apl_list, label="Area per Lipid")
    average_1000 = plt.plot(time_average, apl_average, label="Average APL per ns")
   
    plt.legend()    
    
    x_min = min(time)
    x_max = max(time)
    y_max = max(apl_list)   
    #print("min is:", x_min, "max is:", x_max)

    plt.xlabel('Time (ns)', fontsize = 'large')
    plt.ylabel('Area per lipid (nm ^ 2)', fontsize = 'large')
    plt.xlim(x_min, x_max)
    plt.ylim(0, 0.4)
    plt.suptitle(title, fontsize = '16')
    plt.legend(fontsize = 'large')
    plt.show()
    

#radial_distribution_function ();
	#do I need this? https://en.wikipedia.org/wiki/Radial_distribution_function



#def actual_analysis ():
# just copy pasting the relevant commands that make it work. noteL these are bash commands. 
#gmx traj -s premd2.gro -n index.ndx -f md_295.xtc -z -y -x -ob md295_box
#gmx traj -s md295.gro -n index.ndx -f md_305.xtc -z -y -x -ob md305_box

clean_xvg = xvg_read(xvg)
time, apl_list, time_average, apl_average = apl_function(clean_xvg)
traj_pyplot(time, apl_list, xvg, time_average, apl_average)
