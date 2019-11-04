
# Feature engineering: convert each electrode's ts data into sub-variables of mean, max, min, std for classifier
def GeneralFE(number_of_electrodes, dataframe, col_name):
    
    masterlist = []
    for i in range(int(number_of_electrodes)):
        masterlist.append([])
    
    for i in range(len(s08['buttonpress_events_hg'])):
        for j in range(int(number_of_electrodes)):
            masterlist[j].append(s08['buttonpress_events_hg'][i].T[j])

    test_dataset2=pd.DataFrame()
    test_dataset2['outcome']=s08['outcome']
    test_dataset2['choice.class']=s08['choice.class']
    for j in range(int(number_of_electrodes)):
        test_dataset2['buttonpress_events_hg_e'+str(j)]=pd.Series(masterlist[j])

    for j in range(int(number_of_electrodes)):
        series = test_dataset2['buttonpress_events_hg_e'+str(j)]        
        meanlist=[]
        maxlist=[]
        minlist=[]
        stdlist=[]
        for k in range(len(series)):
            meanlist.append(series[k].mean())
            stdlist.append(series[k].std())
            maxlist.append(series[k].max())
            minlist.append(series[k].min())
        test_dataset2['mean'+str(j)]=meanlist
        test_dataset2['max'+str(j)]=maxlist
        test_dataset2['min'+str(j)]=minlist
        test_dataset2['std'+str(j)]=stdlist
    
    return test_dataset2
