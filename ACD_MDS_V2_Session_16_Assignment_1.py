# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 07:32:16 2018

@author: Eliud Lelerai
"""

import numpy as np
import pandas as pd

# Creating the dataframe


rent_data={'id':list(range(6)),'rent':['$1550', '$1700', '$900', '$850', '$1000', '$950']}

rent_df=pd.DataFrame(rent_data)

rent_df.dtypes

# clean the rent column of $ sign and change dtype to float

rent_df['rent']=rent_df['rent'].str.replace(r'[^\w\s]+', '')
rent_df=rent_df.rename(columns={'rent':'rent_in_usd'})
rent_df['rent_in_usd']=rent_df['rent_in_usd'].astype(float)
rent_df.dtypes

# getting the mean and standard deviation.

print(rent_df['rent_in_usd'].mean())
print(rent_df['rent_in_usd'].std())
