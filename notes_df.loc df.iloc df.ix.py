
# coding: utf-8

# In[124]:


### pandas.DataFrame.loc 
# select rows by label/index or select rows with boolean/conditional lookup.
# df.loc[index, column_name] or df.loc[i,j] # where i references to index values and j references columns values.

import pandas as pd
import os
os.chdir('C:\\Users\\yaffy\\Desktop\\DS\\Database')
x = pd.ExcelFile('gdplev.xls')
df = x.parse(skiprows=5)
df = df[214:]
df = df[['Unnamed: 4','GDP in billions of current dollars.1','GDP in billions of chained 2009 dollars.1']]
df.reset_index(inplace=True)
df = df.drop(['index'],axis=1)
df.head()


# In[108]:


df.loc[0] # return a pd.Series object consisting of all columns for the first row.


# In[39]:


df.loc[0,'Unnamed: 4'] # 1st row + a certain columns


# In[125]:


df.loc[:,'GDP in billions of chained 2009 dollars.1'] # all rows + a certain columns


# In[113]:


df.loc[0:1,'Unnamed: 4': 'GDP in billions of chained 2009 dollars.1'] # frist 2 rows + from 1st to 3rd cols (Multiple)
df.loc[[0,2],['Unnamed: 4', 'GDP in billions of chained 2009 dollars.1']] # 1st, 3rd rows + 1st,3rd cols (Multiple)


# In[44]:


df.loc[(df['Unnamed: 4'] >= '2008Q3') & (df['Unnamed: 4'] <= '2009Q2')] # return all col for rows where from 2008Q3 to 2009Q2


# In[47]:


df.loc[df['Unnamed: 4'] == '2008Q3', 'GDP in billions of current dollars.1'] # return a certain col for rows where 'Unnamed:4' is '2008Q3'


# In[77]:


### pandas.DataFrame.iloc 
# Select rows and columns by number
# df.iloc[i,j] 

df.iloc[0] # first row


# In[85]:


df.iloc[0,0] # 1st row + 1st col


# In[86]:


df.iloc[:, -1] # all rows + last col


# In[92]:


df.iloc[0:2,0:2] # frist 2 rows + from 1st to 2nd cols (Multiple)


# In[94]:


df.iloc[[0,3,4],[0,2]] #1st,4th, 5th rows + 1st,3rd cols (Multiple)


# In[114]:


df.iloc[0,0]


# In[127]:


### More On 
x = pd.ExcelFile('gdplev.xls')
df = x.parse(skiprows=5)
df = df[214:]
df = df[['Unnamed: 4','GDP in billions of current dollars.1','GDP in billions of chained 2009 dollars.1']]
df.set_index(['Unnamed: 4'],inplace=True)
df.head()


# In[128]:


df.loc['2008Q3',:] # label-based indexing using df.loc; whihc df.iloc cannot do.  


# In[142]:


df.loc['2000Q3']['GDP in billions of current dollars.1'] # df.loc[][] equals to df.loc[i,j]
df.iloc[2][0] # df.iloc[][] equals to df.iloc[i,j]

