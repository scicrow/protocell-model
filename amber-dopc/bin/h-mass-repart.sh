#!/bin/bash
#
# hmassrepartition
# Perform hydrogen mass repartitioning.
# 
# Perform hydrogen mass repartitioning on the specied topology. 
# Hydrogen mass repartitioning means that for a given heavy atom, the mass of 
# all bonded hydrogens are increased (to 3.024 u by default) and the mass of that heavy atom 
# is decreased so as to maintain the same overall mass. 
# The main use case is to allow longer time steps for molecular dynamics integration 
# due to reduced frequency of vibration of bonds to hydrogen atoms.
# 
# taken from: https://amberhub.chpc.utah.edu/hmassrepartition/

# hmassrepartition [parm <name> | crdset <set> | parmindex <#> | <#>] [<mask>] [hmass <hydrogen new mass>] [dowater]
#
# [parm <name>] 		Modify topology selected by name.
# [crdset<set>] 		Modify topology of COORDS set.
# [parmindex <#> | <#>] 	Modify topology selected by index <#> (starting from 0).
# [<mask>] 			Atoms to modify (all solute atoms by default).
# [hmass <hydrogen new mass>] 	Mass to change hydrogens to (3.024 u by default).
# [dowater] 			If specified, modify water hydrogen mass as well.

# actually only need to first two but I'm leaving the rest as blank variables so I know what can be put in.
TOPOLOGY=()
COORDS=()
STARTFROM=()
MASK=()
HMASS=()
DOWATER=()

hmassrepartition $TOPOLOGY | $COORDS 
