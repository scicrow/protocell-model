#!/bin/bash
#this program uses awk to find lines with specific molecule names in pdb file and change their resnames to match. 

awk '
    NR > 6774 && match($4, /DECA/) {
         int_var = $5
		 print $int_var
	}
' deca_100mm_nacl.pdb > out.pdb

