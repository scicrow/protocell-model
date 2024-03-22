#!/bin/bash
#These steps I would run either on WSL or directly in the terminal on Setonix
#Create index file
(echo 'r DECN'; echo 'r DECA | r DECN'; echo 'r TIP3 | r SOD | r CLA'; echo 'name 10 Water_and_ions'; echo q) | gmx make_ndx -f min2.gro -o index.ndx