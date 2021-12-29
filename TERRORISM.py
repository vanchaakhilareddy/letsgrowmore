#!/usr/bin/env python
# coding: utf-8

# # DATA SCIENCE INTERN AT LETSGROWMORE - LGMVIP 2021

# ## Task4: Exploratory Data Analysis on Dataset-Terrorism (Intermediate Level)

# ## Name: Akhila Reddy Vancha

# In[5]:


# Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)


# In[6]:


#READING THE DATA
data = pd.read_csv('globalterrorismdb_0718dist.csv',low_memory=False)


# In[17]:


data.head()


# In[18]:


data.tail()


# In[20]:


data.columns.values


# In[21]:


#renaming the columns
data.rename(columns={'iyear':'Year','imonth':'Month','extended':'Extended','iday':'Day','country_txt':'Country','provstate':'State','region_txt':'Region','attacktype1_txt':'AttackType','target1':'Target','nkill':'Killed','nwound':'Wounded','summary':'Summary','gname':'Group','targtype1_txt':'Target_type','weaptype1_txt':'Weapon_type','motive':'Motive','city':'City','latitude':'Latitude','longitude':'Longitude'}, inplace=True)


# In[22]:


#cleaning the data
data=data[['Year','Month','Extended','Day','Country','State','Region','City','Latitude','Longitude','AttackType','Killed','Wounded','Target','Summary','Group','Target_type','Weapon_type','Motive']]


# In[23]:


data.describe()


# In[24]:


data['Region'].value_counts()


# In[25]:


plt.figure(figsize = (20,5))
sns.barplot(data['Region'].value_counts()[:15].index,data['Region'].value_counts()[:15].values,palette='tab10')
plt.title('Most Affected Region')
plt.xlabel('Regions')
plt.ylabel('Count')
plt.xticks(rotation = 90)


# In[26]:


pd.crosstab(data.Year, data.Region).plot(kind='line',figsize=(20,10))
plt.title('Terrorist Activities by Region in each year')
plt.ylabel('Number of Attacks')
plt.grid()
plt.xticks([1970,1975,1980,1985,1990,1995,2000,2005,2010,2015,2017])


# ### Conclusion:-

# ### Most Affected Region->Middle East & North Africa

# ### Least Affected Region->Australasia & Oceania

# In[28]:


#Top 10 Affected Countries:


# ### Conclusion:- Most Affected Country-> Iraq

# In[29]:


# Overall States
data['State'].value_counts()


# In[30]:


plt.figure(figsize = (20,6))
sns.barplot(data['State'].value_counts()[:10].index,data['State'].value_counts()[:10].values)
plt.title('Top 10 Affected States (Overall)')
plt.xlabel('States')
plt.ylabel('Counts')


# ### Conclusion: Most Affected state = Baghdad

# ## In India
# 

# In[31]:


# States of India
df_istates=data[data['Country']=='India']['State']
df_istates.value_counts()


# In[32]:


plt.figure(figsize = (30,10))
sns.barplot(df_istates.value_counts()[:].index,df_istates.value_counts()[:].values)
plt.title('Affected States (India)')
plt.xlabel('States')
plt.ylabel('Counts')


# ### Conclusion :

# ### Most Affected state in India = Jammu and Kashmir

# ### Least Affected state in India = Puducherry

# ## In Pakistan

# In[33]:


df_astates=data[data['Country']=='Pakistan']['State']
df_astates.value_counts()


# In[34]:


plt.figure(figsize = (20,5))
sns.barplot(df_astates.value_counts()[:].index,df_astates.value_counts()[:].values)
plt.title('Affected States (Pakistan)')
plt.xlabel('States')
plt.ylabel('Counts')
plt.xticks(rotation = 90)


# ### Conclusion:

# ### Most Affected state in Pakistan = Balochistan

# ### Least Affected state in Pakistan = Sindh

# In[ ]:





# ## Number of Terrorist Activities each Year
# 

# In[35]:


data['Year'].value_counts()


# In[36]:


plt.figure(figsize = (30,15))
sns.countplot('Year',data=data,palette='tab10')
plt.xticks(rotation = 90)
plt.title('Number of Terrorist Activities each Year')
plt.xlabel('Year')
plt.ylabel('Counts')


# ### Conclusion:-

# ### Highest number of attacks -- 2014

# ### Lowest number of attacks -- 1971

# In[ ]:





# ## Attack Methods:-

# In[37]:


plt.figure(figsize = (20,6))
sns.countplot(data['AttackType'],order = data['AttackType'].value_counts().index,palette='tab10')
plt.title('Attack Methods')
plt.xlabel('Methods')
plt.ylabel('Counts')
plt.xticks(rotation = 90)


# ### Conclusion:-

# ### Least of the attack types= Hijacking

# ### Most of the attack types = Bombing/Explosion

# In[ ]:





# ## Target Types
# 

# In[39]:


plt.figure(figsize = (20,6))
sns.countplot(x="Target_type", data=data, order=data["Target_type"].value_counts().index)
plt.title('Types of Targets')
plt.xticks(rotation = 90)


# ### Most Target type = Private Citizens & Property
# 

# In[ ]:





# ### Frequent Groups Invloved in Terrorist Activity

# In[40]:


data['Group'].value_counts()


# In[41]:


plt.subplots(figsize = (20,10))
sns.barplot(y=data['Group'].value_counts()[:5].index, x=data['Group'].value_counts()[:5].values, palette='tab10')
plt.title('Most Active Terrorist Organizations')


# ### Conclusion Most Active Terrorism Organization is Unknown ,Taliban

# In[ ]:




