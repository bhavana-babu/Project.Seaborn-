#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew
import warnings
warnings.filterwarnings("ignore")


# In[4]:


a=pd.read_csv("heart.csv")


# In[56]:


a


# In[25]:


a.head(10)


# In[26]:


a.tail(10)


# In[27]:


a.info()


# In[28]:


a.size


# In[29]:


a.shape


# In[30]:


#statistical analysis
a.describe()


# In[31]:


a.isnull().sum()


# Conclusions: 
#     
# 1) Each column contains 303 values 
# 2) Mean value is identified for each column 
# 3) The std is standard deviation, if std is close to 0 indicates that the data point re very close to the mean, 
#    whereas a large std indicates data points are spread further away from mean 
# 4) The minimum value of data point in each column 
# 5) Maximum value of data point in each column 
# 6) 25%,50% and 75% of data

# Skewness is a measure of asymmetry in a probability distribution
# 
# 1. Skewness = 0 (normally distributed)
# 2. Skewness > 0 (then more part of data in the left tail of the distribution)
# 3. Skewness < 0 (then more part of data in the right tail of the distribution)

# In[40]:


print(skew(a,axis=0,bias=True))


# Data Visualization

# In[47]:


for i in a.columns:
    sns.distplot(a[i])
    plt.show()


# In[48]:


a.corr()


# In[52]:


pic=plt.figure(figsize=(14,7),dpi=100)
sns.heatmap(a.corr(),annot=True)


# In[59]:


sns.pairplot(data=a,vars=['age','chol','trestbps','sex'],hue='target')


# Analysis Based on Cholesterol Level, Age and Heart Disease
# 
# Relationship between age and heart disease

# In[60]:


sns.catplot(x='target',y='age',kind="boxen",data=a)


# In[61]:


sns.catplot(x='target',y='chol',kind="boxen",data=a)


# In[62]:


sns.relplot(x='chol',y='age',hue='target',data=a)


# Conclusions:
#      
# 1. The dataset says that most of the heart disease rate is between age 50 to 60
# 
# 2. The dataset says that most of the heart disease rate is increased based on the cholestrol level of 200 to 300
# 
# 3. Description: Results are given in milligrams per deciliter (mg/dL). Here are the ranges for total cholesterol in adults: Normal: 
#     Less than 200 mg/dL.. Borderline high: 200 to 239 mg/dL
#         
#     From the above analysis the cholesterol range of the patient in our dataset is above 200. That means cholesterol is high and 
#     the age range is between 40 to 60
#     
#     Treatment: Check the range of cholesterol and follow a healty diet and prevent Heart disease.
#         
#     plenty of vegetables, fruit and wholegrains. a variety of healthy protein-rich foods (especially fish and seafood), legumes 
#     (such as beans and lentils), nuts and seeds. Smaller amounts of eggs and lean poultry can also be included in a heart-healthy 
#     eating pattern."

# In[5]:


sns.catplot(x='target',y='trestbps',kind="boxen",data=a)


# # ANALYSIS BASED ON RESTING BLOOD PRESSURE, AGE AND HEART DISEASE

# In[11]:


sns.catplot(x='target',y='trestbps',kind='violin',data=a)


# In[14]:


sns.relplot(x='trestbps',y='age',hue='target',data=a)


# In[ ]:


Conclusion:

A normal blood pressure level is less than 120/80 mmHg.
The resting blood pressure varies from 120 to 140 range and having age between 40 to 60.


# # ANALYSIS BASED ON MAXIMUM HEART RATE ACHIEVED,AGE AND HEART DISEASE
# 

# In[15]:


sns.catplot(x='target',y='thalach',kind='bar',data=a)


# In[16]:


sns.relplot(x='thalach',y='age',hue='target',data=a)


# # ANALYSIS BASED OF HEART BEAT, AGE, AND HEART DISEASE

# In[23]:


a["Heart Beat"]=220-a["age"]
a.head()


# In[31]:


target_value=a[a["target"]==1]


# In[29]:


sns.relplot(x="age",y="Heart Beat",hue="target",data=a)


# In[32]:


target_value


# In[33]:


target_value=a[a["target"]==0]


# In[34]:


target_value


# Description: You can estimate your maximum heart rate based on your age. To estimate your maximum age-related heart rate, subtract your age from example, for a 50-year-old person, the estimated maximum age-related heart rate would be calculated as 220-50 years = 170 beats per minute (bpr
# 
# In our dataset maximum heart rate in between 160 to 220 and age 40 to 70 range.
# 
# Conclusion:
# 
# 1) if the age is 40, 220-40 180 is the maximunm heart rate based calculation, the dataset says that, person having o 40 range of age having heart rate of 200 beats per min.
