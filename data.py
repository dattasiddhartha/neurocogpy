import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

# input of user is directory and .mat file

# functions
## load mat file
## merge files, csv and mat

from scipy.io import loadmat
def Parser(dir2, mat_file, col):
    df11 = loadmat(os.path.join(dir2, mat_file))
    eeg_data=pd.DataFrame()
    col1=[]
    for i in range(len(df11['buttonpress_events_hg'])):
        col1.append(col[i])
    eeg_data['col1']=col1
    return eeg_data

def MatToJson(dir2, mat_file, col):
    df11 = loadmat(os.path.join(dir2, mat_file))
    eeg_data=pd.DataFrame()
    col1=[]
    for i in range(len(df11['buttonpress_events_hg'])):
        col1.append(col[i])
    eeg_data['col1']=col1
    eeg_data.to_json('s08_data.json')