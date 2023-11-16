#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model


# In[3]:


df=pd.read_excel("homeprices.xlsx")
df


# In[4]:


#let us take median of it for bedrooms 
df.bedrooms.median()


# In[7]:


#3.5 is float but we need in interger so let us import math and use it
import math
med_bedrooms=math.floor(df.bedrooms.median())
med_bedrooms


# In[9]:


# let us fill NaN value as 3
df.bedrooms.fillna(med_bedrooms)


# In[10]:


# let us update in the df
df.bedrooms=df.bedrooms.fillna(med_bedrooms)
df


# In[12]:


#now let us train the model
reg=linear_model.LinearRegression()
reg.fit(df[['area','bedrooms','age']],df.price)
#remember area,bedrooms,age are independent variables and price is targeted value


# In[13]:


reg.coef_
#we are finding coefficients of area bedrooms age (m1,m2,m3)


# In[15]:


reg.intercept_
#we are finding intercepts (b)


# In[16]:


# now let us predict the value of 3000 sqrft,3 bedrooms,40 years old
reg.predict([[3000,3,40]])


# In[18]:


#let us find the value of it by calculating it 
137.25*3000+-26025*3+-6825*40+383724.9999999998


# In[19]:


# now let us predict the value of 2500 sqrft,4 bedrooms,5 years old
reg.predict([[2500,4,5]])


# In[20]:


#let us find the value of it by calculating it 
137.25*2500+-26025*4+-6825*5+383724.9999999998


# In[ ]:




