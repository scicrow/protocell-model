#!/bin/bash
#this program uses awk to find lines with specific molecule names in pdb file and change their resnames to match. 

awk '{
    if (match($0, /TIP3/)) {
	    printf "%sTIP3%s\n", substr($0, 1, 72), substr($0, 73)
    } else if (match($0, /SOD/)) {
	    printf "%sSOD%s\n", substr($0, 1, 72), substr($0, 73)
    } else if (match($0, /CLA/)) {
	    printf "%sCLA%s\n", substr($0, 1, 72), substr($0, 73)
	} else {
        print $0
    }
}' testing.pdb > out2.pdb

