import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB

buttonpress_events_hg_e1=[]
buttonpress_events_hg_e2=[]
buttonpress_events_hg_e3=[]
buttonpress_events_hg_e4=[]
buttonpress_events_hg_e5=[]
for i in range(len(s08['buttonpress_events_hg'])):
    for j in range(len(s08['buttonpress_events_hg'][i])):
        buttonpress_events_hg_e1.append(s08['buttonpress_events_hg'][i][j][0])
        buttonpress_events_hg_e2.append(s08['buttonpress_events_hg'][i][j][1])
        buttonpress_events_hg_e3.append(s08['buttonpress_events_hg'][i][j][2])
        buttonpress_events_hg_e4.append(s08['buttonpress_events_hg'][i][j][3])
        buttonpress_events_hg_e5.append(s08['buttonpress_events_hg'][i][j][4])