import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

# Visualize Electrode eeg time series for one column
## Generates a series of time graphs, each graph represents each electrode at each time step
def Visualizer(columnname, eeg_data1):
    testdata=eeg_data1[columnname]
    for j in range(len(testdata)):
        subrow=testdata[j]
        fig = plt.figure(figsize=(15, 10))
        for i in range(5):
            testdata0=subrow[:, [i]]
            t=range(len(testdata0))
            ax = fig.add_subplot(5,6,i+1)
            plt.plot(t, testdata0)
            plt.title("electrode"+str(i))    
        plt.tight_layout()
        plt.show()
        
        
def Periodicity(col):
    timeserieslist=[]
    for i in range(len(col)):
        for j in range(len(col[i])):
            timeserieslist.append(col[i][j])       
    timeseriesdata=np.concatenate(timeserieslist)
    from statsmodels.tsa.seasonal import seasonal_decompose
    series = timeseriesdata
    result = seasonal_decompose(series, model='additive',freq=3001)
    result.plot()
    plt.show()