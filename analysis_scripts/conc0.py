#!/usr/bin/python

W_atom = 11562
K_atom = 0
#conc_305 = 0.1
#while(conc_305 < 0.2):
#    W_atom = W_atom - 2
#    K_atom = K_atom + 1
#
#    avagadro = 6.022 * 10 ** 23
#
#    #moles of each
#    W_mol = W_atom / avagadro
#    K_mol = K_atom / avagadro
#    W_atom_mass = 18.01528 #g/mol
#
#    W_mass = W_atom_mass * W_mol # result is grams
#
#    #density values taken from https://www.engineeringtoolbox.com/water-density-specific-weight-d_595.html?vA=295&units=K#
#    W_density_295 = 0.9978 * 1000 #g/L
#    W_density_305 = 0.9951 * 1000 #g/L
#
#    vol_W295 = W_mass / W_density_295 
#    vol_W305 = W_mass / W_density_305
#
#
#
#    #print ("volume at 295 is", vol_W295)
#    #print ("volume at 305 is", vol_W305)
#
#    conc_295 = K_mol / vol_W295
#    conc_305 = K_mol / vol_W305 #mol/L

decanoics = 288
total_pot = K_atom + 144
print ("number of water atoms at 305K is", W_atom, "number of salt ions is", K_atom)
print ("total number of potassium ions is", total_pot)
print ("ratio of lipids to water", decanoics / W_atom)
#print ("concentration of salt ions at 295K is:", conc_295, "mol/L")
#print ("concentration of salt ions at 305K is:", conc_305, "mol/L")



