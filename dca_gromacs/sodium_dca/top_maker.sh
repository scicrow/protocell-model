#!/bin/bash

gmx pdb2gmx -f deca_100mm_nacl.pdb -o pdbgmx.gro -p topol.top -i toppar/forcefield.itp -n index.ndx 
