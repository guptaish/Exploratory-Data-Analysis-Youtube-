#!/usr/bin/env python
# coding: utf-8

# In[57]:


import numpy as np
import pandas as pd
data=pd.read_csv('Datasets/INvideos.csv')
data

#Cleaning Data
dlt=['trending_date','video_error_or_removed','comments_disabled','thumbnail_link','ratings_disabled']
data=data.drop(dlt,axis=1)
data.info()

#removing duplicates
data=data.drop_duplicates(keep='first')
data


# In[2]:


#Exploratory Analysis


# In[3]:


import seaborn as sns
import matplotlib.pyplot as plt

sns.pairplot(data)
plt.show()


# In[4]:


columns_of_interest = ['views', 'likes', 'dislikes','comment_count']
corr_matrix = data[columns_of_interest].corr()
corr_matrix


# In[5]:


#Top viewed video


# In[6]:


top=data.sort_values(by=['views'],ascending=False)
top=top.drop_duplicates(subset='video_id',keep='first')
top=top.head(10)

print(top[['title','views']])
plt.bar(top['title'],top['views'])
plt.xticks(rotation=90)
plt.show()


# In[7]:


#Most Liked video


# In[8]:


liked=top=data.sort_values(by=['likes'],ascending=False)
liked=liked.drop_duplicates(subset='video_id',keep='first')
liked=liked.head(10)
plt.bar(liked['title'],liked['likes'])
plt.xticks(rotation=90)
plt.show()


# In[9]:


#Most disliked viedo


# In[10]:


disliked=data.sort_values(by=['dislikes'],ascending=False)
disliked=disliked.drop_duplicates(subset='video_id',keep='first')
disliked=disliked.head(10)
plt.bar(disliked['title'],disliked['dislikes'])
plt.xticks(rotation=90)
plt.show()


# In[11]:


#Most commented video


# In[12]:


comments=data.sort_values(by=['comment_count'],ascending=False)
comments=disliked.drop_duplicates(subset='video_id',keep='first')
comments=comments.head(10)
plt.bar(comments['title'],comments['comment_count'])
plt.xticks(rotation=90)
plt.show()


# In[13]:


#Top viewed channels


# In[21]:


new=data.groupby('channel_title').sum().sort_values(by=['views'],ascending=False)
fig, ax = plt.subplots(figsize=(15,7))
new.plot(ax=ax)
new
# plt.plot(new['channel_title'],new['views'],c='green')
# plt.plot(new['channel_title'],new['likes'],c='black')
# plt.plot(new['channel_title'],new['dislikes'],c='orange')
# plt.show()


# In[22]:


#Adding Category column using json


# In[61]:



categories_df = pd.read_json('Datasets/IN_category_id.json')

data['category_id'] = data['category_id'].astype(str)
id_to_category = {}
for category in categories_df['items']:
    id_to_category[category['id']] = category['snippet']['title']
data.insert(4, 'category', data['category_id'].map(id_to_category))    


# In[69]:


cate=data.groupby('category').sum().sort_values(by=['views'],ascending=False)
fig, ax = plt.subplots(figsize=(15,7))
cate['views'].plot.bar(ax=ax,color=['r', 'g', 'b','orange','lightgreen'])
cate

