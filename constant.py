# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np 	#Array		
import matplotlib.pyplot as plt		
import pandas as pd			
#--------------------------------------------
# import the dataset & divided my dataset into independe & dependent
dataset = pd.read_csv(r"Downloads\Data.csv")
X = dataset.iloc[:, :-1].values	
y = dataset.iloc[:,3].values  
#--------------------------------------------
from sklearn.impute import SimpleImputer # SPYDER 4 
##imputer = SimpleImputer()  # hyperparameter tunning
imputer = SimpleImputer(missing_values=np.nan, strategy='constant')

imputer = SimpleImputer()
#imputer = Imputer(missing_values = 'NaN',strategy = 'mean',axis =0) #spyder
#-----------------------------------------------------------------------------
imputer = imputer.fit(X[:,1:3]) 
X[:, 1:3] = imputer.transform(X[:,1:3])