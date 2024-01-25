#!/bin/bash

module unload cray-libsci
# load either openblas
module load openblas/0.3.21
# or netlib
#module load netlib-lapack/<version> netlib-scalapack/<version>
