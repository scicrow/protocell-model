#!/bin/bash
#bilayer builder. a packmol script 

# runs a membrane builder for protonated (DECA) and unprotonated (DECN) deconoic acid. filepaths hardcoded
# original script:
# R:\A-J\Biomolecular_Model-MANCER-HS00092\Origins_of_life\JAMES_EXTRA\Documents\amber_systems\packmol_reorder
# \bilayer\salt_only\bilayer_0mM\bilayer_0mM.inp

# check any generated pdb file to make sure the heads are around the correct way.
# especially from charmm, this might not occur.
#
# you can generate individual itp files using charmm gui membrane builer
# https://www.charmm-gui.org/?doc=input/converter.ffconverter&step=2

echo "building membrane..."

packmol < bilayer_0mm.inp > bilayer_0mm.out

echo "membrane building complete."
