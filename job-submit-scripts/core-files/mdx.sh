#!/bin/bash

run_dir=$(pwd)
core_dir=$run_dir"/core-files"

echo "Running $core_dir/run_lib.py"
python3 $core_dir/run_lib.py "min" "gmx" $core_dir $run_dir
