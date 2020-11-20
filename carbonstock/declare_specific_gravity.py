#!/usr/bin/env python
# coding: utf-8
import pandas as pd
def fill_wsg(df1, path_to_wsg_df = './data'):
    print(path_to_wsg_df)
    df2 = pd.read_csv(path_to_wsg_df, header=None)
    df2.columns = ['botanical name', 'specific gravity']
    df = df1.merge(df2, how='left', on='botanical name')
    if 'specific gravity_x' in df.columns:
        df['specific gravity'] = [wsg_x if not pd.isnull(wsg_x) else wsg_y
                                  for (wsg_x, wsg_y) in zip(df['specific gravity_x'], df['specific gravity_y'])
                                 ]
        df.drop(columns=['specific gravity_x', 'specific gravity_y'], inplace=True)
    return df
path_data = "./data/"
df = pd.read_csv(path_data+"measures.csv")
df['botanical name'] = [name[name.find('-')+2:] for name in df['Specie']]
df['common name'] = [name[:name.find('-')-1] for name in df['Specie']]
df.columns = ['name', 'seeds', 'trees', 'use', 'diameter', 'height', 'density', 'AGB',
       'source', 'botanical name', 'common name']
df.drop(columns='density', inplace=True)
df.sort_values(by='botanical name', inplace=True, ignore_index=True)
paths_sources = [
    path_data+"wagnermeters/mydata.csv",
    path_data+"maniatisetal2011/table4.csv",
    path_data+"tamangetal2019/table1.csv",
    path_data+'milesandsmith2009/table4.csv',
]
for source in paths_sources:
    df = fill_wsg(df,source)
df.to_csv(path_data+'ourforest.csv')
