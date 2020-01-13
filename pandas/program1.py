#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 15:18:06 2018

@author: manasisubhedar
"""
import pandas
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as ss
from scipy.stats import norm

#importing csv file

df2 = pandas.read_csv('hw3q2.csv') 

print("QUESTION 2a")
df2.boxplot()
plt.savefig('boxplot.jpg')
plt.title("Q2A: Fig1 for Boxplot for question Q2a")
plt.xlabel("Given dataset")
plt.ylabel("Values")
plt.show()

#question 2b
print("QUESTION 2b")

x = df2.applymap(np.log2)
x.boxplot()
plt.title("Q2B: Fig2 for Boxplot for question Q2b")
plt.xlabel('Given dataset')
plt.ylabel('log2 transformed data')
plt.show()


# 2c Summary Statistics of the data

print("QUESTION 2C")
print(" Summary Statistics of the Data")
stats = df2.describe()
print(stats)


#2D

print("Question 2d:Histogram ")
np.log(df2).hist(density = 'True', bins=20)
plt.show()

#2e
print("QUESTION 2E")
print("Plot A is a lognormal distribution")
print("Plot B is a Normal distribution")
print("Plot C is a Pareto distribution")
print("Plot D is a Exponential distribution")

#2f 
#Normal Probability Plot'
data_a = df2.a.tolist()
data_a.sort()

ss.probplot(data_a,plot=plt) 

plt.xlabel(' Standard normal ')
plt.ylabel('Column a ')
plt.title('Q2F: Normal Probability Plot')
plt.show()

#Normal distribution
data_b = df2.b.tolist()
data_b.sort()

fit = norm.pdf(data_b, np.mean(data_b), np.std(data_b))
plt.plot(data_b,fit,'-o')

plt.xlabel('Column b ')
plt.ylabel(' PDF ')
plt.title('Q2F: Normal distribution')
plt.show()


#Exponential Distribution
data_c = df2.c.tolist()
data_c.sort()

plt.plot(np.exp(data_c),1-np.array(data_c))

plt.xlabel(' Column c')
plt.ylabel(' CCDF ')
plt.title('Q2F: Exponential Distribution')
plt.show()


#Pareto Distribution
data_d = df2.d.tolist()
data_d.sort()

plt.plot(np.random.pareto(data_d),1-np.array(data_d))

plt.xlabel(' Column d')
plt.ylabel(' CCDF ')
plt.title('Q2F: Pareto Distribution')
plt.show()




 


