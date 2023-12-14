#!/bin/bash
export AMBERHOME=/home/packages/amber20
/home/packages/amber20/bin/pmemd.cuda -O -i min.in\
 -p tc5b.1l2y.hmass.parm7 -c tc5b.1l2y.rst7 -o min.out\
 -x min.crd -inf min.info -r min.rst7\




