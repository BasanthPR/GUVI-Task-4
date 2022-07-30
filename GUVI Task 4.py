#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
d1=pd.read_csv("college_1.csv")
d1.head()


# In[8]:


d2=pd.read_csv("college_2.csv")
d2.head()


# In[10]:


d1.describe()


# In[11]:


d2.describe()


# In[16]:


y=pd.concat([d1,d2],ignore_index=True)
y.head()


# In[18]:


y.describe()


# In[21]:


y.info()


# if 10000<codekata score<15000 (Reached_expectations.csv)

# In[22]:


v=y[y['CodeKata Score']>15000]
v


# if 10000<codekata score<15000 (Reached_expectations.csv)

# In[23]:


p=y[(y['CodeKata Score']>10000)&(y['CodeKata Score']<15000)]
p


# if 7000<codekata score<10000 (Needs_Improvement.csv)

# In[24]:


c=y[(y['CodeKata Score']>7000)&(y['CodeKata Score']<10000)]
c


# if codekate score < 7000 (Unsatisfactory.csv)

# In[26]:


b=y[y['CodeKata Score']<7000]
b


# Average of previous week geekions vs this week geekions (i.e Previous Geekions vs CodeKata Score)
# 

# In[28]:


pre=y['Previous Geekions'].mean()
pre 


# In[29]:


sco=y['CodeKata Score'].mean()
sco


# In[30]:


res=sco-pre
res


# As per results we found that the CodeKata Score average is 209.41 more than previous geek coins

# No of students participated

# In[33]:


tot=y.count()
tot


# 119 students were participated in both colleges
# 

# Average completion of python course,my_sql,python english and computational thinking
# 

# In[35]:


my=y['mysql'].mean()
ct=y['computational_thinking'].mean()
pe=y['python_en'].mean()
p=y['python'].mean()
my,ct,pe,p


# Rising star of the week (top 3 candidate who performed well in that particular week)
# 
# 1)shifak N
# 
# 2)Ganesh Ramkumar R
# 
# 3)Narasimhan Y L

# In[36]:


f=y.sort_values(by = 'Rising',ascending = False)
f.head(3)


# Shining stars of the week (top 3 candidates who has highest geek cions)
# 
# 1)A.Dharani
# 
# 2)V.JEEVITHA
# 
# 3)HEMAVATHI.R

# In[37]:


s=y.sort_values(by = 'Previous Geekions',ascending = False)
s.head(3)


# Department wise codekata performence (pie chart)
# 

# In[46]:


y.groupby(['Department']).sum().plot(kind='pie', y = 'CodeKata Score',figsize=(10,10),autopct=('%1.1f%%'));


# In[48]:


x=['A.Dharani-CSE','Bodipudi Harini-ECE','ASHOK KUMAR K-EEE']
y=[24500,10040,19400]
plt.bar(x, y)
plt.xlabel("Department wise toppers")
plt.ylabel("codekata score")
plt.title("Vertical bar graph")
plt.show()

