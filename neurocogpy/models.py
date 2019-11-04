
# Classification models for class-based decision-making tasks
def ModelBundle(X, Y):
    
    from sklearn.svm import SVC, LinearSVC
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.ensemble import AdaBoostClassifier
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.naive_bayes import GaussianNB
    from sklearn.linear_model import Perceptron
    from sklearn.linear_model import SGDClassifier
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.model_selection import train_test_split
    from sklearn import linear_model
    from sklearn.metrics import confusion_matrix
    from sklearn.metrics import precision_score
    from sklearn.metrics import recall_score

    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=100)
    print ('Number of samples in training data:',len(x_train))
    print ('Number of samples in test data:',len(x_test))

    # Name our logistic regression object
    LogisticRegressionModel = linear_model.LogisticRegression()

    # we create an instance of logistic Regression Classifier and fit the data.
    print ('Training a logistic Regression Model..')
    LogisticRegressionModel.fit(x_train, y_train)

    training_accuracy=LogisticRegressionModel.score(x_train,y_train)
    print ('Training Accuracy:',training_accuracy)

    test_accuracy=LogisticRegressionModel.score(x_test,y_test)
    print('Accuracy of the model on unseen test data: ',test_accuracy)

    #CONFUSION MATRIX
    y_true = y_test
    y_pred = LogisticRegressionModel.predict(x_test)
    ConfusionMatrix=pd.DataFrame(confusion_matrix(y_true, y_pred),columns=['Predicted Gamble','Predicted Safe'],index=['Actual Gamble','Actual Safe'])
    print ('Confusion matrix of test data is: \n',ConfusionMatrix)   
    print("Average precision for the 2 classes is - ", precision_score(y_true, y_pred, average = None) )
    print("Average recall for the 2 classes is - ", recall_score(y_true, y_pred, average = None) )
    
    return LogisticRegressionModel

