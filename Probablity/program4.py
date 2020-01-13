#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 22:17:32 2018

@author: manasisubhedar
"""
#Question 4a
import pandas as pd
import math
import decimal
import matplotlib.pyplot as plt
import numpy as np
import statistics
import pandas
    

def summaryStatistics(listOfNums):
    i = 1
    j = 1
    squareDiffList = []
    summaryStat = []
    
    
 #Calculate maximum number in the list
    maxNum = listOfNums[0]
    while (i < (len(listOfNums))) :
            if(maxNum < (listOfNums[i])) :
                maxNum = listOfNums[i]
            i = i+1
        
 #Calculate minimum number in the list
    minNum = listOfNums[0]
    while (j < (len(listOfNums))):
            if(minNum > (listOfNums[j])) :
                minNum = listOfNums[j]
            j = j+1
        
 #Calculate mean in the list
    mean = sum(listOfNums) / len(listOfNums)
        
        #Calculate median in the list
    sortListOfNums = sorted(listOfNums)
    if((len(sortListOfNums) % 2) == 1 ) :         #if list is odd
            midLen = len(sortListOfNums)//2
            median = sortListOfNums[midLen]
    else :                                       #if list is even
            midLen = len(sortListOfNums)//2
            median = (sortListOfNums[midLen-1] + sortListOfNums[midLen]) / 2
       
        
#standard Deviation in the list
    j = 0
    meanOfNum = sum(listOfNums) / len(listOfNums)
    while (j < (len(listOfNums))):
            squareDiffList.append((listOfNums[j] - meanOfNum)**2)
            j = j+1
    meanSquareDiff = sum(squareDiffList) / len(listOfNums)
    standardDeviation= math.sqrt(meanSquareDiff)
      
        
#75th percentile in the list
    sortListOfNums = sorted(listOfNums)
    indexVal = (0.75) * (len(listOfNums))
    number = decimal.Decimal(indexVal)
    indexVal = int(number.quantize(decimal.Decimal('1'), rounding='ROUND_HALF_UP'))
    Percentile75 = sortListOfNums[indexVal-1]
        
    
#25th percentile in the list
    sortListOfNums = sorted(listOfNums)
    indexVal = (0.25) * (len(listOfNums))
    number = decimal.Decimal(indexVal)
    indexVal = int(number.quantize(decimal.Decimal('1'), rounding='ROUND_HALF_UP'))
    Percentile25 = sortListOfNums[indexVal-1]
                     
    summaryStat = {'Maximum Number':maxNum,'Minimum Number':minNum,'Mean':mean,'Median':median,'Standard Deviation':standardDeviation,'75th Percentile':Percentile75,'25th Percentile':Percentile25}
    return (summaryStat) 
   
if __name__ == '__main__':


    data = pd.read_csv('brfss.csv', index_col=0)

    data = data.drop('wtkg2',axis=1).dropna(axis=0, how='any').values
    
    current_weight = list(data[:,1])
    weight_a_year_ago = list(data[:,2])
    height = list(data[:,3])
    age = list(data[:,0])
    sex = list(data[:,4])
    
    
    
    ssA = summaryStatistics(current_weight)
    ssB = summaryStatistics(weight_a_year_ago)
    ssC = summaryStatistics(height)

Lists = ["current_wt","wt_a_year_ago","height"]
ListRange = range(len(Lists))
ListLoc = [20,20,140]
    
ssA = list(ssA.values())
meanA = ssA[2]
stdA  = ssA[4]
ssA[4] = meanA + stdA
ssA.insert(5,meanA - stdA)
ssB = list(ssB.values())
meanB = ssB[2]
stdB  = ssB[4]
ssB[4] = meanB + stdB
ssB.insert(5,meanB - stdB)
ssC = list(ssC.values())
meanB = ssC[2]
stdC  = ssC[4]
ssC[4] = meanB + stdC
ssC.insert(5,meanB - stdC)

MaxList =[ssA[0],ssB[0],ssC[0]]
MinList =[ssA[1],ssB[1],ssC[1]]
MeanList =[ssA[2],ssB[2],ssC[2]]
MedianList =[ssA[3],ssB[3],ssC[3]]
SdList1 =[ssA[4],ssB[4],ssC[4]]
SdList2 =[ssA[5],ssB[5],ssC[5]]
PerList1 =[ssA[6],ssB[6],ssC[6]]
PerList2 =[ssA[7],ssB[7],ssC[7]]
    
plt.figure(1)
plt.xticks(ListLoc,Lists)
plt.scatter(ListRange,MaxList,c='k',marker='1')
plt.scatter(ListRange,MinList,c='k',marker='2')
plt.scatter(ListRange,MeanList,c='b',marker='+')
plt.scatter(ListRange,MedianList,c='b',marker='x')
plt.scatter(ListRange,SdList1,c='g',marker='1')
plt.scatter(ListRange,SdList2,c='g',marker='2')
plt.scatter(ListRange,PerList1,c='r',marker='1')
plt.scatter(ListRange,PerList2,c='r',marker='2')
     
plt.xticks(ListRange,Lists)
plt.title("Summary Statistics graph")
plt.xlabel("Data Set")
plt.ylabel("Statistics Range")
plt.legend(['Max','Min','Mean','Median','Mean+SD','Mean-SD','75 Per','25 Per'],loc='upper right',fontsize='8')
plt.show()
plt.savefig('Summary Statistics.jpeg')


#Question 4b
#age = data.age

weight_change = [x1 - x2 for (x1, x2) in zip(current_weight, weight_a_year_ago)]
empty_array = []

for row in weight_change: 
    empty_array.append(row)
    
cor_Current_weight = np.corrcoef(weight_change,current_weight)[0, 1]
print ("\nCorrelation between weight change and current weight: ", cor_Current_weight)

cor_wt_yr_ago = np.corrcoef(weight_change,weight_a_year_ago)[0, 1]
print("\nCorrelation between weight change and weight year ago is:", cor_wt_yr_ago)

cor_age = np.corrcoef(weight_change,age)[0, 1]
print("\nCorrelation between weight change and current age is:", cor_age)

positive_Corr_Current_weight = abs(cor_Current_weight)
positive_Corr_wt_yr_ago = abs(cor_wt_yr_ago)
positive_Corr_age = abs(cor_age)

list_of_coefficients = [positive_Corr_Current_weight,positive_Corr_wt_yr_ago,positive_Corr_age]
list_of_coefficients.sort()
max_value = list_of_coefficients[2]
print("\nMaximum value is", max_value, ", weight change and weight year ago are most correlated.")

plt.scatter (weight_change, current_weight, label='Weight change & Current weight', color='r', marker='o')
plt.scatter (weight_change, weight_a_year_ago,label='Weight change & Weight year ago', color='g', marker='*')
plt.scatter (weight_change, age,label='Weight change & Age', color='b', marker='.')
plt.title("Correlation between Weight change and other CSV columns", fontsize = 10)
plt.xlabel("WEIGHT CHANGE")
plt.ylabel("WEIGHT IN KG")

plt.legend(prop={'size': 6})
plt.show()


#Question 4c


male_indices=[i for i,x in enumerate(sex) if x==1]
female_indices=[i for i,x in enumerate(sex) if x==2]


male_current_weight=[]
male_weight_a_year_ago=[]
male_height=[]

for item in male_indices:
    male_current_weight.append(current_weight[item])
    male_weight_a_year_ago.append(weight_a_year_ago[item])
    male_height.append(height[item])
    
weight_change_male = [x1 - x2 for (x1, x2) in zip(male_current_weight, male_weight_a_year_ago)]

mean_male_wt_chng=np.mean(weight_change_male)
SEM_male_wt_chng=np.std(weight_change_male)/math.sqrt(len(weight_change_male))
print("mean of male weight changes {r}".format(r=mean_male_wt_chng))
print("mean of female weight changes {r}".format(r=SEM_male_wt_chng))



female_current_weight=[]
female_weight_a_year_ago=[]
female_height=[]

for item in male_indices:
    female_current_weight.append(current_weight[item])
    female_weight_a_year_ago.append(weight_a_year_ago[item])
    female_height.append(height[item])
    
weight_change_female = [x1 - x2 for (x1, x2) in zip(female_current_weight, female_weight_a_year_ago)]

mean_female_wt_chng=np.mean(weight_change_female)
SEM_female_wt_chng=np.std(weight_change_female)/math.sqrt(len(weight_change_female))
print("mean of male weight changes {r}".format(r=mean_female_wt_chng))
print("mean of female weight changes {r}".format(r=SEM_female_wt_chng))



#Question 4d

import random
from random import sample


weight_change = [x1 - x2 for (x1, x2) in zip(current_weight, weight_a_year_ago)]

empty_list = []
for row in weight_change:
    empty_list.append(row)

array_sex = []    
for row in sex:
    array_sex.append(row)
   
male_sex = array_sex[int(len(array_sex)/2):]
female_sex = array_sex[int(len(array_sex)/2):]

t_test_list = []

for i in range(1000):
        
    weight_change1 = empty_list[int(len(empty_list)/random.randint(2, 4)):]
    weight_change2 = empty_list[:int(len(empty_list)/random.randint(2, 4))]
    
    weight_change_male = sample(weight_change1,len(weight_change1))
    weight_change_female = sample(weight_change2,len(weight_change2))
    
    
    mean_male = statistics.mean(weight_change_male)
    SD_male = statistics.stdev(weight_change_male)
    variance_male = statistics.variance(weight_change_male)
    
    mean_female = statistics.mean(weight_change_female)
    SD_female = statistics.stdev(weight_change_female)
    variance_female = statistics.variance(weight_change_female)
    
    t_test_value = abs(mean_male-mean_female)/(math.sqrt((variance_male/len(weight_change_male))+(variance_female/len(weight_change_female))))
    t_test_list.append(t_test_value)  


t_test_list.sort()
plt.hist(t_test_list)
plt.title("Distribution of -log10(p-value)")
plt.xlabel('-log10(p-value)')
plt.ylabel('t-test values')
plt.show()
    

    


#question 4e


weight_height_ratio = current_weight/height

WHR_list = []

male=[]
female=[]


for row in weight_height_ratio:
    WHR_list.append(row)
    
for i in WHR_list:
    index = WHR_list.index(i)
    if sex[index] == 1:
        male.append(i)
    
    else:
        female.append(i)
        
mean_male = statistics.mean(male)
mean_female = statistics.mean(female)

SD_male = statistics.stdev(male)
SD_female = statistics.stdev(female)

variance_male = statistics.variance(male)
variance_female = statistics.variance(female)

length_male = len(male)
length_female = len(female)

t_test_value = abs(mean_male-mean_female)/(math.sqrt((variance_male/length_male)+(variance_female/length_female)))
print("t-test value is: ",t_test_value)


sex_list=[] 
for row in sex:
    sex_list.append(row)

male_sex=[i for i,x in enumerate(sex) if x==1]
female_sex=[i for i,x in enumerate(sex) if x==2]

t_test_list = []

for i in range(2):
        
    WHR1 = WHR_list[int(len(WHR_list)/random.randint(2, 4)):]
    WHR2 = WHR_list[:int(len(WHR_list)/random.randint(2, 4))]
    
    weight_height_sample1 = sample(WHR1,len(WHR1)) 
    weight_height_sample2 = sample(WHR2,len(WHR2))

    mean1 = statistics.mean(weight_height_sample1)
    SD1 = statistics.stdev(weight_height_sample1)
    variance1 = statistics.variance(weight_height_sample1)
    
    mean2 = statistics.mean(weight_height_sample2)
    SD2 = statistics.stdev(weight_height_sample2)
    variance2 = statistics.variance(weight_height_sample2)

    t_test_value = abs(mean1-mean2)/(math.sqrt((variance1/len(weight_height_sample1))+(variance2/len(weight_height_sample2))))
    t_test_list.append(t_test_value)


t_test_list.sort()
plt.hist(t_test_list)
plt.title("Distribution of -log10(p-value)")
plt.xlabel('-log10(p-value)')
plt.ylabel('Probability of t-test value')
plt.show()





































