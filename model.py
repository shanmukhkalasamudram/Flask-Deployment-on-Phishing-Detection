# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier 
import seaborn as sns
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split,cross_val_score

dataset = pd.read_csv('phishing.csv')


X = np.array(dataset.iloc[:,1:31])

y = np.array(dataset.iloc[:,31:])



train_X,test_X,train_Y,test_Y=train_test_split(X,y,test_size=0.3,random_state=2)


from sklearn.tree import DecisionTreeClassifier

decision=DecisionTreeClassifier()



test = decision.fit(train_X,train_Y)



# Saving model to disk
pickle.dump(test, open('model.pkl','wb'))

