#!/bin/bash
filename=$@

#ssh -i ~/.ssh/pawsey_ssh tcrow@setonix.pawsey.org.au

scp -r $file_name tcrow@data-mover.pawsey.org.au:/scratch/pawsey0110/tcrow
