#!/bin/python

import numpy as np
import matplotlib.pyplot as plt
import sys

def xvg_read(xvg):
    #reading the gromacs xvg file and pulling the coords
    with open(xvg, 'r') as f:
         out_read = f.readlines()
    
    out_read = out_read[25:] #first 25 lines is junk text.
    return (out_read)


def run_pyplot(out_table, ions_list, lipid_list):
    n = 0
    for out in out_table:
        data = np.loadtxt(out)
        position = data[:,0]
        dcadcn = data[:,1]
        ions = data[:,2]
        plt.plot(position, dcadcn, label = lipid_list[n])
        plt.plot(position, ions, label = ions_list[n])
        n = n + 1

    plt.xlabel('Distance (nm)', fontsize = 'large')
    plt.ylabel('Density (kg/m^3)', fontsize = 'large')
    plt.xlim(-2, 2)
    plt.ylim(0, 1000)
    plt.suptitle('Density of lipids and Merz ions', fontsize = '16')
    plt.legend(fontsize = 'large')
    plt.show()
    
path_name = ["/home/thomas/md-runs-archive/MerzFF/01-19-15-10_Kions/", "/home/thomas/md-runs-archive/MerzFF/01-19-15-16_NaMerz/"]
temp_name = ["density_295K.xvg", "density_305K.xvg"]
path_array = [path + temp for path in path_name for temp in temp_name]
#print(path_array)


ions_list = ['potassium ions @ 295K', 'potassium ions @ 305K', 'sodium ions @ 295K', 'sodium ions @ 305K']
lipid_list = ['DCA/DCN @ 295K (K ions)', 'DCA/DCN @ 305K (K ions)', 'DCA/DCN @ 295K (Na ions)', 'DCA/DCN @ 305K (Na ions)']

out_table = []
for x in path_array:
    out = xvg_read(x)
    out_table.append(out)

run_pyplot(out_table, ions_list, lipid_list)
#print(data_table[0])


