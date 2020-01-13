#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 16:46:48 2018

@author: manasisubhedar
"""

import pandas as pd
import numpy as np
#import scipy.stats as sp
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
#from sklearn.linear_model import LinearRegression 


hdfstore = pd.HDFStore('hw3q3.h5')


#3a

print("Question 3A:")

X = hdfstore['x']
y = hdfstore['y']
model= LinearRegression()
model.fit(X, y)

y2 = model.predict(X)
SS_Residual = sum((y-y2)**2)
SS_Total = sum((y-np.mean(y))**2)
r_squared = 1 - (float(SS_Residual))/SS_Total
print("r-square:",r_squared)

y_true = y 
y_predict = model.predict(X)
mse = mean_squared_error(y_true , y_predict)
print("Mean Square Error:", mse)


ValueofX= [0, 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
Beta = model.coef_
Alpha = model.intercept_
xAxis = range(len(ValueofX)) 
plt.bar(xAxis, Beta)
plt.xticks(xAxis , ValueofX)
plt.ylabel('Value of Coefficients')
plt.title('Q3A: Calculated coefficients')
plt.show()


#3b - Bootstrap 

coef = list(hdfstore.coef)
x = list(hdfstore.coef)
pvalue = [(i/0.4) for i in coef]
pvalue.sort()

b = range(len(pvalue))

plt.bar(pvalue,b,width = 0.3)

plt.xlabel("-log10(pvalue)")
plt.ylabel(" Values ")
plt.title("Q3B: Bar chart for Statistical Significance")
plt.show()


#3c
print("Question 3C:")

index = 0
alpha_values = []
coefList = []
r_squaredList = []
mse = []
alpha_range= [-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6]
for i in range(-6,6):
    model = Lasso(alpha= 2**i)
    X1 = hdfstore['x']
    y1 = hdfstore['y']
    model.fit(X1,y1)
    beta_lasso = model.coef_
    #r-squared 
    y2 = model.predict(X1)
    SS_Residual = sum((y1-y2)**2)
    SS_Total = sum((y1-np.mean(y1))**2)
    r_squared = 1 - (float(SS_Residual))/SS_Total
    mean_sq = mean_squared_error(y1, y2)
    r_squaredList.insert(index,r_squared)
    mse.insert(index,mean_sq)
    alpha_values.insert(index,2**i)
    coefList.insert(index,sum(beta_lasso))
    index = index+1

#plot coefficients alpha and beta
plt.semilogx(alpha_values,coefList, '-or')
plt.semilogx(alpha_values,r_squaredList, '-og')
plt.semilogx(alpha_values,mse, '-ob')
plt.ylabel('Value of Coefficient')
plt.title('Q3C: Lasso Regresion')
plt.show()


#3d
print("Question 3D:")
model = LinearRegression()
x = hdfstore['sf']
newX = X / x
model.fit(newX , y)

#r-squared 
y2 = model.predict(newX)
Residual = sum((y-y2)**2)
Total = sum((y-np.mean(y))**2)
r_squared = 1 - (float(Residual))/Total
print("r-square Value is ",r_squared)

#mean square error
mse = mean_squared_error(y, y2)
print("Mean Square Error Value is ", mse)

#plot coefficients alpha and beta
Beta = model.coef_
Alpha = model.intercept_
ValueofX= [0, 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
xAxis = range(len(ValueofX)) 
plt.bar(xAxis, Beta)
plt.xticks(xAxis , ValueofX)
plt.ylabel('Coefficient values')
plt.title('Q3D: Calculated coefficients')
plt.show()