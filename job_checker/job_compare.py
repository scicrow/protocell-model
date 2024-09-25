#!/usr/bin/env python
"""SCRIPT FOR CHECKING IF JOBS ARE CURRENTLY RUNNING VIA DATAFRAME COMPARISON"""
#import os
#import re
#pip install datacompy
#import numpy as np
# NEEDS:
# module load py-pandas/2.1.2
import pandas as pd

def read_log(log_file):
    """READ RUNNING OR PENDING JOBS OF SACCT AND SQUEUE"""
    
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    df=pd.DataFrame()

    with open(log_file, 'r', encoding='utf-8') as f:
        content = f.readlines() 
    
    for line in content:
        line = (line.strip("\n").split())
        new_row = pd.Series(line)
        df = pd.concat([df, new_row.to_frame().T], ignore_index=True)
    
    # FILTER OUT TRIPLICATE JOBIDS THAT ARE PRINTED IN SACCT
    substring = '.'
    filter = df['JobID'].str.contains(substring)
    filtered_df = df[~df['JobID'].str.contains(r'\.')]
    filtered_df = filtered_df.sort_values(by=['JobID'])
    df.columns=['JobID', 'JobName','Status']    
    
    return(filtered_df)

def read_job_his(log_file):
    """READ RUNNING OR PENDING JOBS OF SACCT AND SQUEUE"""
    
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    jdf = pd.DataFrame()

    with open(log_file, 'r', encoding='utf-8') as f:
        content = f.readlines() 
    
    for line in content:
        line = (line.strip("\n").split())
        new_row = pd.Series(line)
        jdf = pd.concat([jdf, new_row.to_frame().T], ignore_index=True)
    
    # FILTER OUT TRIPLICATE JOBIDS THAT ARE PRINTED IN SACCT
    #filtered_df = jdf.sort_values(by=['JobID'])    
    jdf.columns = ['JobID', 'DirName']
    jfiltered_df = jdf
    filtered_df = filtered_df.sort_values(by=['JobID'])
    return(jfiltered_df)

# VARIABLES
sacct_log = "upsacct.log"
job_his = "jobhis.log"

# RUN FUNCTIONS
sacct_df = read_log(sacct_log)
job_df = read_job_his(job_his)
