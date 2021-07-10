#!/usr/bin/env python
# coding: utf-8

# ### Question 4

# In[1]:


import pandas as pd 
import numpy as np
import missingno as msno
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


# I read the data
df = pd.read_csv("country_vaccination_stats.csv")


# In[3]:


df


# In[4]:


df.info()


# In[5]:


# I checked null values
msno.matrix(df)


# In[6]:


# The number of null values
df.isnull().sum()


# In[7]:


df.head()


# In[8]:


# Grouped by countries minimum values
df.groupby("country")["daily_vaccinations"].min()


# In[9]:


# Filling in null values with minimum values grouped by country
df["daily_vaccinations"].fillna(df.groupby("country")["daily_vaccinations"].transform("min"),inplace=True)


# In[10]:


# Confirm 
df[df["country"]=="Belgium"]


# In[11]:


df.loc[0]


# In[12]:


df.isnull().sum()


# In[13]:


# Kuwait dosen't have any vaccinations value. I fill it with 0(zero)
df[df["daily_vaccinations"].isnull()]


# In[14]:


df.fillna(0,inplace=True)


# In[16]:


df.isnull().sum()


# ### Question 5

# In[33]:


df.head()


# In[41]:


median = df.groupby("country")["daily_vaccinations"].median()
median


# In[48]:


median.sort_values(ascending=False).head(3)


# ### Question 6

# In[ ]:


df.head()


# In[ ]:


df[df["date"]=="1/6/2021"]["daily_vaccinations"].sum()


# In[ ]:





# In[ ]:




