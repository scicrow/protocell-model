#!/bin/bash

TOPOLOGY=*repart.prmtop 
COORDS=*inpcrd

parmed -n -p $TOPOLOGY -c $COORDS --prompt minimize 

