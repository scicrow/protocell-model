#!/bin/python

import numpy as np
import matplotlib.pyplot as plt
import sys
import pandas as pd

xvg = sys.argv[1]
print("input file is:", xvg) 

def xvg_read(xvg):
    #reads a gromacs density xvg file and removes the comments and starting blurb to the file
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
            
        print(clean_xvg)

    return (clean_xvg)



def frame_xvg(clean_xvg):
    #this makes dataframes (like csv files). not implemented
    xvg_frame = pd.DataFrame(clean_xvg)
    print(xvg_frame)
    


def run_pyplot(clean_xvg, xvg):
    title = xvg.strip(".xvg")
    figure_file = title + ".png"
    title = "C14 mass density profile of: " + title

    print(figure_file)
    position = []
    lipid = []
    pot = []
    cla = []
    tip3p = [] 
    
    for line in clean_xvg:
        position.append(float(line[0]))
        lipid.append(float(line[1]))
        pot.append(float(line[2]))
        cla.append(float(line[3]))
        tip3p.append(float(line[4]))
        

    lipid_line =  plt.plot(position, lipid, label='Lipids')
    pot_line = plt.plot(position, pot, label='Potassium')
    cla_line = plt.plot(position, cla, label='Chloride')
    sol_line = plt.plot(position, tip3p, label='Solution')
    plt.legend()    
    
    x_min = min(position)
    x_max = max(position)
    y_max = max(tip3p)   
    print("min is:", x_min, "max is:", x_max)

    plt.xlabel('Distance (nm)', fontsize = 'large')
    plt.ylabel('Density (kg/m^3)', fontsize = 'large')
    #plt.xlim(x_min, x_max)
    #plt.ylim(-10, 10)
    plt.suptitle(title, fontsize = '16')
    plt.legend(fontsize = 'large')
    plt.show()
    
#print(path_array)



clean_xvg = (xvg_read(xvg))
run_pyplot(clean_xvg, xvg)

