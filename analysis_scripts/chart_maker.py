#!/bin/python

import numpy as np
import matplotlib.pyplot as plt



def xvg_read(xvg):
    #reading the gromacs xvg file and pulling the coords
    with open(xvg, 'r') as f:
         out_read = f.readlines()
    print(xvg)
    out_read = out_read[29:] #first 29 lines is junk text.
    print(len(out_read))
    time, apl_list = list_maker(out_read)
    return(time, apl_list)


def list_maker(out_read):
    # pulls the dimensions and time from the xvg file for use in pyplot.
    time_list = [] # time in ps
    x_list = [] # x length in nm (y is same in semiistropic system)
    z_list = [] # z length in nm (not the same as x and y in semiisotropic system)
    apl_list = []
    for i in out_read:
        i = i.split('\t')
        #print(i)
        time = float(i[1])
        time = time / 1000 # converting ps to ns
        time_list.append(time)
        x_length = (i[2])
        x_length = float(x_length)
        area = x_length ** 2
        area = area / 288
        apl_list.append(area)
        x_list.append(x_length)
        z_list.append(i[4])
    return(time_list, apl_list)

#python plot for apl will be number of lipids = 288 divided by the area which is x**2 - y**2
   
def run_pyplot(time, Na_apl_295, Na_apl_305, K_apl_295, K_apl_305):
    x_ticks = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    fig, (axs1, axs2) = plt.subplots(2, sharex=True, sharey=True)
    fig.text(0.05, 0.35, 'Area per lipid (nm**2)', ha='center', fontsize='large', rotation='vertical')
    fig.suptitle('Bilayer stability in 100mM salt solution: Merz ion FF', fontsize='16')

    axs1.set_title('Bilayer area per lipid in NaCl solution')
    axs1.plot(time, Na_apl_295, color='r', label="295 K")
    axs1.plot(time, Na_apl_305, color='b', label="305 K")
    axs1.legend()

    axs2.set_title('Bilayer area per lipid in KCl solution')
    axs2.plot(time, K_apl_295, color='r', label="295 K")
    axs2.plot(time, K_apl_305, color='b', label="305 K")

    plt.xlabel('Simulation time (ns)')
    plt.axis((0, 10, 0.1, 0.2))
    plt.xticks(x_ticks)
    plt.show()

time = []
apl_295 = []
timeNa295, Na_apl_295 = xvg_read("01-19-15-16_NAions_md295box.xvg") 
timeNa305, Na_apl_305 = xvg_read("01-19-15-16_NAions_md305box.xvg") 

timeK295, K_apl_295 = xvg_read("Kions_md295_box.xvg") 
timeK305, K_apl_305 = xvg_read("Kions_md305_box.xvg") 

print('Na 295K: ', len(timeNa295), 'ns', len(Na_apl_295), 'apl entries')
print('Na 305K: ', len(timeNa305), 'ns', len(Na_apl_305), 'apl entries')

print('K 295K: ', len(timeK295), 'ns', len(K_apl_295), 'apl entries')
print('K 305K: ', len(timeK305), 'ns', len(K_apl_305), 'apl entries')

run_pyplot(timeNa295, Na_apl_295, Na_apl_305, K_apl_295, K_apl_305)
