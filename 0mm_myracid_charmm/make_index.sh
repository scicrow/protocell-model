#!/bin/bash

coord_in=$@

commands = """
r DCN
r DCA | r DCN
r SOL | r K  | r CL
name 10 Water_and_ions
q 
"""
   
echo '{commands}' | gmx make_ndx -f {coord_in} -o index.ndx