#!/bin/python
# Thomas Crow

import numpy as np
import matplotlib.pyplot as plt
import sys

xvg = sys.argv[1]

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
    
    tot_apl_av = sum(apl_list)/len(apl_list)
    print("average apl over time is", tot_apl_av)
    return(time, apl_list)
    

clean_xvg = xvg_read(xvg)
time, apl_list = apl_function(clean_xvg)
