#!/usr/bin/env python
# coding: utf-8

# In[14]:


# In this code, I want to categorize United states counties by Hospital Beds capacity (number of beds per 1000)
# during Covid-19 pandemic into 5 levels.

import pandas as pd
import numpy as np

df = pd.read_csv('hospital_beds_USA_v1.csv')

# In this step, I set the 'county' column as the index, then use groupby() to 
# have data in groups of uniqe counties (which is 1850 in this dataset).
# Then I select 'beds' from columns and use agg() and numpy to have a
# series of counties and their average number of beds per 1000.

df = df.set_index('county').groupby(level = 0)['beds'].agg(np.average)

# Output is series of 1850 counties and their average number of beds per 1000.

# Now, I want to make a category of Hospitals with pandas.cut().

cat = pd.cut(df,5)

# The output is 5 interval catagories : [(-0.0302, 6.04] < (6.04, 12.081] < (12.081, 18.121] < (18.121, 24.161] < (24.161, 30.201]]

# To make it more readable, I label 5 categories
# in which ['E' < 'D' < 'C' < 'B' < 'A']

cat = pd.cut(df,5, labels = ['E','D','C','B','A'])


# Now, I want to count the number of each category.

print('''
        The number of A hospitals is: {0} 
        The number of B hospitals is: {1} 
        The number of C hospitals is: {2} 
        The number of D hospitals is: {3} 
        The number of E hospitals is: {4} '''.format(  
        len(cat[cat == 'A']) , len(cat[cat == 'B']) ,
        len(cat[cat == 'C']) , len(cat[cat == 'D']), 
        len(cat[cat == 'E'])))

#The output is : The number of A hospitals is: 2 
#The number of B hospitals is: 5 
#The number of C hospitals is: 11 
#The number of D hospitals is: 47 
#The number of E hospitals is: 1785 

# Therefore, just 2 counties in USA had Hospital Beds capacity (number of beds per 1000) in A level, which is (24.161, 30.201].


# In[ ]:





# In[ ]:




