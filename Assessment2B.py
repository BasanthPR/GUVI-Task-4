#!/usr/bin/env python
# coding: utf-8

# ###### Assessment

# ###### I am going to provide two .csv files , you are supposed to work on them and have to provide solutions to the following problems

# ###### import necessary libraries

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt


# ###### merge those two csv files (after getting as dataframes, get them as a single dataframe)

# In[3]:


df1=pd.read_csv('college_1.csv')
df2=pd.read_csv('college_2.csv')
df = pd.concat([df1,df2], ignore_index=True)
df


# ###### Take each csv file , split that csv file into multiple categories (example csv files are added in the repo) 
# 

# ###### consider if the codekata score exceeds 15000 points(present week) then make a csv on those observations as Exceeded expectations.csv
# 

# In[4]:


df3 = df[df['CodeKata Score']>15000]

df3.to_csv('Exceeded expextations1.csv')

df4 = pd.read_csv("Exceeded expextations1.csv")
df4


# In[5]:


df4.shape


# In[6]:


df3.shape


# ###### if  10000<codekata score<15000   (Reached_expectations.csv)
# 
# 

# In[7]:


df7 = df[(df['CodeKata Score'] > 10000) & (df['CodeKata Score'] < 15000)]
df7.to_csv('Reached_expectations.csv')

df8 = pd.read_csv("Reached_expectations.csv")
df8.shape


# ###### if  7000<codekata score<10000   (Needs_Improvement.csv)
# 

# In[8]:


df9 = df[(df['CodeKata Score'] > 7000) & (df['CodeKata Score'] < 10000)]

df9.to_csv('Needs_Improvement1.csv')

df9 = pd.read_csv("Needs_Improvement1.csv")
df9.shape


# ###### if  codekate score < 7000        (Unsatisfactory.csv)

# In[9]:


df5 = df[df['CodeKata Score']<7000]

df5.to_csv('Unsatisfactory.csv')

df6 = pd.read_csv("Unsatisfactory.csv")
df6.shape


# ###### Average of previous week geekions vs this week geekions (i.e Previous Geekions vs CodeKata Score)

# In[10]:


avg_1 = df['Previous Geekions'].mean()
avg_2 = df['CodeKata Score'].mean()

avg_diff = avg_2 - avg_1
avg_diff


# ###### No of students participated 

# In[11]:


df4 = df['Name'].count()
df4


# ###### #Average completion of python course or my_sql or python english or computational thinking

# In[14]:


a = df['mysql'].mean()
b=df['python'].mean()
c=df['python_en'].mean()
d=df['computational_thinking'].mean()
a,b,c


# ###### rising star of the week (top 3 candidate who performed well in that particular week)

# In[15]:


df.nlargest(3, ['Rising'])


# ###### Shining stars of the week (top 3 candidates who has highest geekions)

# In[16]:


df.nlargest(3, ['Previous Geekions'])


# ###### Department wise codekata performence (pie chart)

# In[33]:


df.groupby(['Department']).sum().plot(kind='pie', y = 'CodeKata Score',figsize=(10,10),autopct=('%1.1f%%'));


# ###### Department wise toppers (horizantal bar graph or any visual representations of your choice)

# In[35]:


x=['A.Dharani-CSE','Bodipudi Harini-ECE','ASHOK KUMAR K-EEE']
df=[24500,10040,19400]
plt.bar(x, df)
plt.xlabel("Department wise toppers")
plt.ylabel("codekata score")
plt.title("Vertical bar graph")
plt.show()

