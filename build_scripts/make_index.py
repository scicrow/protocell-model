#!/bin/python
import subprocess

commands = """
r LAUP | r LAU 
r TIP3 | r POT |r CLA 
q 
"""
   
#name 6 TIP3_POT
subprocess.run(f"echo '{commands}' | gmx make_ndx -f lau_100mm_kcl.gro -o index.ndx", shell=True)
