# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 22:00:02 2024

@author: C_FA0142
"""

import pandas as pd

df = pd.read_csv('sales.csv',index_col='month')

month_df = df.loc[['apr ','may','jun'],]
egg_df = month_df['eggs']>100
egg_count = egg_df.sum()
final_df = (df.loc[['apr ','may','jun'],]['eggs']>100).sum()
# noloc_df = df[['apr ','may','jun']]
new_df = df['eggs']