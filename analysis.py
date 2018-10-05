import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB

def FiveElectrodeNaiveBayes(outcome_column_name):
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
    test_dataset=pd.DataFrame()
    test_dataset['outcome']=s08['outcome']
    test_dataset['buttonpress_events_hg_e1']=pd.Series(buttonpress_events_hg_e1)
    test_dataset['buttonpress_events_hg_e2']=pd.Series(buttonpress_events_hg_e2)
    test_dataset['buttonpress_events_hg_e3']=pd.Series(buttonpress_events_hg_e3)
    test_dataset['buttonpress_events_hg_e4']=pd.Series(buttonpress_events_hg_e4)
    test_dataset['buttonpress_events_hg_e5']=pd.Series(buttonpress_events_hg_e5)

    gnb = GaussianNB()
    used_features =[
        "buttonpress_events_hg_e1",
        "buttonpress_events_hg_e2",
        "buttonpress_events_hg_e3",
        "buttonpress_events_hg_e4",
        "buttonpress_events_hg_e5",
        "buttonpress_window_events_hg_e1",
        "buttonpress_window_events_hg_e2",
        "buttonpress_window_events_hg_e3",
        "buttonpress_window_events_hg_e4",
        "buttonpress_window_events_hg_e5",
    ]

    # Train classifier
    gnb.fit(
        test_dataset[used_features].values,
        test_dataset[outcome_column_name]
    )
    y_pred = gnb.predict(test_dataset[used_features])

    # Print results
    print("Number of mislabeled points out of a total {} points : {}, performance {:05.2f}%"
          .format(
              test_dataset.shape[0],
              (test_dataset["outcome"] != y_pred).sum(),
              100*(1-(test_dataset["outcome"] != y_pred).sum()/test_dataset.shape[0])
    ))
