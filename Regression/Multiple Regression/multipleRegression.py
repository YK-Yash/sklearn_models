# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 22:10:08 2017

@author: Dell
"""

# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

# Encoding catagorical data
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelEncoder_X = LabelEncoder()
X[:,3] = labelEncoder_X.fit_transform(X[:,3])
oneHotEncoder = OneHotEncoder(categorical_features = [3])
X = oneHotEncoder.fit_transform(X).toarray()


# Avoiding the dummy variable trap
X = X[:,1:]


# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


# Fitting multiple linear regression into the training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)

# Predicting the test set result
y_pred = regressor.predict(X_test)

# Backward elimination
import statsmodels.formula.api as sm
X = np.append(arr = np.ones((50,1)).astype(int), values =X ,axis = 1)

X_opt = X[:,[0,1,2,3,4,5]]
regressor_ols = sm.OLS(endog = y, exog = X_opt).fit()
regressor_ols.summary()

X_opt = X[:,[0,2,3,4,5]]
regressor_ols = sm.OLS(endog = y, exog = X_opt).fit()
regressor_ols.summary()

X_opt = X[:,[0,3,4,5]]
regressor_ols = sm.OLS(endog = y, exog = X_opt).fit()
regressor_ols.summary()

X_opt = X[:,[0,3,5]]
regressor_ols = sm.OLS(endog = y, exog = X_opt).fit()
regressor_ols.summary()


X_opt = X[:,[0,3]]
regressor_ols = sm.OLS(endog = y, exog = X_opt).fit()
regressor_ols.summary()