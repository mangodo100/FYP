# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 00:23:27 2020

@author: chaur
"""

#part 1: Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

#Part 2: Importing the dataset
dataset = pd.read_csv('FYP_MOD.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 20].values

#Part 3: Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()

#Part 4: Encoding Independant Variable 


onehotencoder = OneHotEncoder()
X[:,0] = labelencoder_X.fit_transform(X[:,0])
X[:,1] = labelencoder_X.fit_transform(X[:,1])
X[:,2] = labelencoder_X.fit_transform(X[:,2])
X[:,3] = labelencoder_X.fit_transform(X[:,3])
X[:,4] = labelencoder_X.fit_transform(X[:,4])
X[:,5] = labelencoder_X.fit_transform(X[:,5])
X[:,6] = labelencoder_X.fit_transform(X[:,6])
X[:,7] = labelencoder_X.fit_transform(X[:,7])
X[:,8] = labelencoder_X.fit_transform(X[:,8])
X[:,9] = labelencoder_X.fit_transform(X[:,9])
X[:,10] = labelencoder_X.fit_transform(X[:,10])
X[:,11] = labelencoder_X.fit_transform(X[:,11])
X[:,12] = labelencoder_X.fit_transform(X[:,12])
X[:,13] = labelencoder_X.fit_transform(X[:,13])
X[:,14] = labelencoder_X.fit_transform(X[:,14])
X[:,15] = labelencoder_X.fit_transform(X[:,15])
X[:,16] = labelencoder_X.fit_transform(X[:,16])
X[:,17] = labelencoder_X.fit_transform(X[:,17])
X[:,18] = labelencoder_X.fit_transform(X[:,18])
X[:,19] = labelencoder_X.fit_transform(X[:,19])


onehotencoder = OneHotEncoder(categorical_features = [0])
onehotencoder = OneHotEncoder(categorical_features = [1])
onehotencoder = OneHotEncoder(categorical_features = [2])
onehotencoder = OneHotEncoder(categorical_features = [3])
onehotencoder = OneHotEncoder(categorical_features = [4])
onehotencoder = OneHotEncoder(categorical_features = [5])
onehotencoder = OneHotEncoder(categorical_features = [6])
onehotencoder = OneHotEncoder(categorical_features = [7])
onehotencoder = OneHotEncoder(categorical_features = [8])
onehotencoder = OneHotEncoder(categorical_features = [9])
onehotencoder = OneHotEncoder(categorical_features = [10])
onehotencoder = OneHotEncoder(categorical_features = [11])
onehotencoder = OneHotEncoder(categorical_features = [12])
onehotencoder = OneHotEncoder(categorical_features = [13])
onehotencoder = OneHotEncoder(categorical_features = [14])
onehotencoder = OneHotEncoder(categorical_features = [15])
onehotencoder = OneHotEncoder(categorical_features = [16])
onehotencoder = OneHotEncoder(categorical_features = [17])
onehotencoder = OneHotEncoder(categorical_features = [18])
onehotencoder = OneHotEncoder(categorical_features = [19])
X = onehotencoder.fit_transform(X).toarray()
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)
y = onehotencoder.fit_transform(y).toarray()



#part 3: Splitting the dataset into the training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

#Part 4: Feature Scaling


#Part 5: Fitting classifier to training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

#Part 6: Predicting the Test set results
pickle.dump(classifier, open('model.pkl','wb'))

model = pickle.load(open('model.pkl', 'rb'))




