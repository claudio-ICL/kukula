#!/usr/bin/env python
# coding: utf-8
# In[1]:
import pandas as pd
path_data = "./data/"
df = pd.read_csv(path_data+"measures.csv")
df['botanical name'] = [name[name.find('-')+2:] for name in df['Specie']]
df['common name'] = [name[:name.find('-')-1] for name in df['Specie']]
df.columns = ['name', 'seeds', 'trees', 'use', 'diameter', 'height', 'density', 'AGB',
       'source', 'botanical name', 'common name']
df.drop(columns='density', inplace=True)
wm = pd.read_csv(path_data+"wagnermeters/cleaneddata.csv", header=None)
wm.columns = ['common name', 'botanical name', 'specific gravity', 'verified']
wm.drop(columns='verified', inplace=True)
df = df.merge(wm, on='botanical name', how='inner', suffixes=[' original',' wagnermeters'])
df.to_csv(path_data+'measures_wagnermeters.csv')
