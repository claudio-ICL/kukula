#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
path_data = "./data/"


# In[2]:


df = pd.read_csv(path_data+"measures.csv")


# In[3]:


df['botanical name'] = [name[name.find('-')+2:] for name in df['Specie']]
df['common name'] = [name[:name.find('-')-1] for name in df['Specie']]


# In[4]:


df.columns = ['name', 'seeds', 'trees', 'use', 'diameter', 'height', 'density', 'AGB',
       'source', 'botanical name', 'common name']


# In[5]:


df.drop(columns='density', inplace=True)


# In[6]:


wm = pd.read_csv(path_data+"wagnermeters/cleaneddata.csv", header=None)
wm.columns = ['common name', 'botanical name', 'specific gravity', 'verified']
wm.drop(columns='verified', inplace=True)


# In[7]:


df = df.merge(wm, on='botanical name', how='inner', suffixes=[' original',' wagnermeters'])


# In[9]:


df.to_csv(path_data+'measures_wagnermeters.csv')


# In[ ]:




