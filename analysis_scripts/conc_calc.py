#!/usr/bin/python

W_atom = 14400
salt_num = 0
conc_305 = 0.0 #starting concentration, not including balancing ions
while(conc_305 < 0.1): #change this float value to the concentration in mM that you want (here is 0.1mM)
    W_atom = W_atom - 2 # removing two water ions as you're going to need a positive and negative ion replacement
    salt_num = salt_num + 1

    avagadro = 6.022 * 10 ** 23

    #moles of each
    W_mol = W_atom / avagadro
    K_mol = salt_num / avagadro
    W_atom_mass = 18.01528 #g/mol

    W_mass = W_atom_mass * W_mol # result is grams

    #density values taken from https://www.engineeringtoolbox.com/water-density-specific-weight-d_595.html?vA=295&units=K#
    W_density_295 = 0.9978 * 1000 #g/L
    W_density_305 = 0.9951 * 1000 #g/L

    vol_W295 = W_mass / W_density_295 
    vol_W305 = W_mass / W_density_305



    #print ("volume at 295 is", vol_W295)
    #print ("volume at 305 is", vol_W305)

    conc_295 = K_mol / vol_W295
    conc_305 = K_mol / vol_W305 #mol/L

decanoics = 288
total_pot = salt_num + 144
print ("number of water atoms at 305K is", W_atom, "number of salt ions is", salt_num)
print ("total number of potassium ions is", total_pot)
print ("ratio of lipids to water", decanoics / W_atom)
print ("concentration of salt ions at 295K is:", conc_295, "mol/L")
print ("concentration of salt ions at 305K is:", conc_305, "mol/L")



