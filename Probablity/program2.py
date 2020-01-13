 -*- coding: utf-8 -*-\
"""\
Created on Mon Sep 10 22:17:32 2018\
\
@author: manasisubhedar\
"""#question 3a\
import matplotlib.pyplot as plt\
import random\
\
fair_coin = ["Head", "Tail"] \
blank_array = []\
total = 0 \
\
for i in range(10**5): \
    list = [random.choice(fair_coin) for _ in range(100)]\
    count = 0\
    for j in list:\
       if j=="Head":\
            count+=1\
            total+=1\
    blank_array.append(count) \
print("Total number of heads:", total)\
blank_array.sort()\
\
plt.hist(blank_array)\
plt.title("Histogram for Heads")\
plt.xlabel('Total Number of Heads')\
plt.ylabel('Total Heads count')\
plt.show()\
print("\\n graph for Q3 \\n")\
\
#question 3a\
\
import numpy as np\
\
\
fair_coin = ["Head", "Tail"] \
array_size = [] \
total = 0 \
\
for i in range(10**5): \
    list = [random.choice(fair_coin) for _ in range(100)]\
    count = 0\
    for j in list:\
       if j=="Head":\
            count+=1\
            total+=1\
    array_size.append(count)\
    \
print("Total number of heads:", total)   \
array_size.sort()\
\
y = np.arange(1, (len(array_size))+1)/len(array_size)\
\
plt.plot(array_size, y)\
\
\
plt.xlabel('Total Number of Heads')\
plt.ylabel('Total Heads count')\
plt.title('CDF')\
plt.margins(0.02)\
\
plt.show()\
print("\\n graph for Question-3a \\n")\
\
#Question 3b\
\
import scipy.stats as ss\
\
fair_coin = ["Head", "Tail"] \
array_list = [] \
prob = [] \
total = 0 \
k=0\
for i in range(10**5):  \
    list = [random.choice(fair_coin) for _ in range(100)]\
    count = 0\
    k+=10\
    for j in list: \
       if j=="Head":\
            count+=1\
            total+=1\
    prob.append(ss.binom._cdf(k,100,0.5))\
\
    array_list.append(count) \
  \
array_list.sort()\
prob.sort()\
\
y = np.arange(1, (len(prob))+1)/len(prob)\
plt.plot(array_list, y, marker = '_')\
plt.yscale('log')\
\
plt.xlabel('Total Number of Heads')\
plt.ylabel('Distribution of Heads count')\
plt.title('Binomial distribution ')\
plt.margins(0.02)\
plt.show()\
print("\\n graph for Question-3b \\n")\
\
\
#question 3c\
\
import matplotlib.pyplot as plt\
import random\
\
\
fair_coin = ["Head", "Tail"] \
blank_array = [] \
total = 0 \
\
for i in range(10**5):  \
    list = [random.choice(fair_coin) for _ in range(100)]\
    count = 0\
    for j in list: \
       if j=="Head":\
            count+=1\
            total+=1\
    blank_array.append(count) \
print("Total number of heads:", total)   \
blank_array.sort()\
\
n = len(blank_array)\
xs= [random.normalvariate(50.0, 5.0) for i in range(n)]\
\
plt.xlabel('Standard normal value')\
plt.ylabel('Heads count range')\
plt.title('Normal Probability Plot')\
\
plt.plot(sorted(xs),sorted(blank_array))\
plt.show()\
print("\\n graph for Question-3c \\n")\
\
# question 3d\
\
import matplotlib.pyplot as plt\
import random\
import scipy.stats as ss\
\
list1 = [random.uniform(0, 1) for _ in range(10**5)]\
random_prob=[]\
for row in list1:\
    random_prob.append(row)\
\
\
fair_coin = ["Head", "Tail"] \
blank_array = [] \
prob = [] \
total = 0 \
k=0\
for i in range(10**5): \
    list = [random.choice(fair_coin) for _ in range(100)]\
    count = 0\
    k+=10\
    for j in list: \
       if j=="Head":\
            count+=1\
            total+=1\
    prob.append(ss.binom._cdf(k,100,0.5))\
    \
    blank_array.append(count) \
blank_array.sort()\
prob.sort()\
\
n = len(blank_array)\
xs= [random.normalvariate(50.0, 5.0) for i in range(n)]\
\
plt.xlabel('Normal Distributed values')\
plt.ylabel('Cumulative probability')\
plt.title('Normal Distribution Approximation')\
plt.yscale('log')\
plt.xscale('log')\
\
plt.plot(sorted(blank_array),sorted(random_prob))\
\
plt.show() \
print("\\n graph for Question-3d \\n")\
\
\
}
