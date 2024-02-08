#!/bin/python

import os

dir_name = os.getcwd()
dir_name = dir_name.split('/')
dir_name = dir_name[-1]
print(dir_name)
