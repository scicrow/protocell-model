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
#
# hmassrepartition [parm <name> | crdset <set> | parmindex <#> | <#>] [<mask>] [hmass <hydrogen new mass>] [dowater]
#
#
# 15.2.2.24. HMassRepartition
#Usage: HMassRepartition [<mass>] [dowater#]
# This action implements hydrogen mass repartitioning in which the mass of each hydrogen is changed to <mass>
# (the default value is 3.024 daltons if no mass is provided). The mass of the heavy atom that the hydrogen is attached
# to is adjusted so that the total mass remains the same. This allows longer time steps to be taken in dynamics (see
# the relevant literature regarding this approach; e.g., [421]). By default, partitioning is only applied to the solute
# since SHAKE on water is handled analytically (via the SETTLE algorithm). 
# Water can be forcibly repartitioned using the keyword dowater.
# from: https://ambermd.org/doc12/Amber21.pdf#page=285
#
#
# [parm <name>] 		Modify topology selected by name.
# [crdset<set>] 		Modify topology of COORDS set.
# [parmindex <#> | <#>] 	Modify topology selected by index <#> (starting from 0).
# [<mask>] 			Atoms to modify (all solute atoms by default).
# [hmass <hydrogen new mass>] 	Mass to change hydrogens to (3.024 u by default).
# [dowater] 			If specified, modify water hydrogen mass as well.
#
# actually only need to first two but I'm leaving the rest as blank variables so I know what can be put in.
TOPOLOGY=(*prmtop)
COORDS=(*inpcrd)
# STARTFROM=()
# MASK=()
# HMASS=()
# DOWATER=()
#
#
#
#
parmed -n -p $TOPOLOGY -c $COORDS -O --prompt HMassRepartition 
# echo $TOPOLOGY $COORDS
