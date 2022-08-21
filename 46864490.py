#!/usr/bin/env python
# coding: utf-8

# In[19]:


#Importing Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
df = pd.read_csv('Input/Epinions_cleaned_data_portfolio_2.csv')
df.head()


# In[6]:


#question 1: the data is already cleaned.
#quesion 2.1: Total number of unique UserId, unique reviews, unique items, and unique categories
print(len(df.userId.unique()))
print(len(df.review.unique()))
print(len(df.item.unique()))
print(len(df.category.unique()))


# In[14]:


#question 2.2: 

print(sum(df.rating)) #Total ratings
print(min(df.rating)) #Minimu ratings
print(max(df.rating)) #Maximum ratings

# Mean of Rating
mean_rating = df['rating'].mean()
print("Mean Rating: ", mean_rating)

#Standard Deviation of Ratings
std_dev_rating = df['rating'].std()
print("Standard deviation in Rating: ", std_dev_rating)


# In[27]:


#question 2.3: 

print(min(df.gender)) #Minimu gender
print(max(df.gender)) #Maximum gender

# Mean of Gender
mean_gender = df['rating'].mean()
print("Mean of Gender: ", mean_gender)


# In[29]:


#question 2.3: 

print(min(df.gender)) #Minimu gender
print(max(df.gender)) #Maximum gender

# Mean of Gender
mean_gender = df['rating'].mean()
print("Mean of Gender: ", mean_gender)


# In[32]:


#question 2.4: 
# total number of ratings per item
df.shape
df.info()


# In[47]:


df["item"] = df1["item"].astype("int64", errors='ignore')


# In[65]:


new_df = df.drop((['review', 'gender', 'category', 'helpfulness','gender','category','userId','timestamp' ]), axis=1)
print(new_df)


# In[82]:


#Question 3:
# Plotting
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns #Seaborn is a Python data visualization library based on matplotlib
sns.set(style="whitegrid")
plt.figure(figsize=(10,8)) #Width, height in inches.
sns.boxplot(x='userId', data= df, orient="h") #https://pythonbasics.org/seaborn-boxplot/  orient“v” | “h”, optional Orientation of the plot (vertical or horizontal). 


# In[85]:


# checking rating for different types of item
plt.figure(figsize=(15,10))
sns.boxplot(x='item', y='rating', data=df, orient="v")


# In[102]:


# checking reviews written by a user
plt.figure(figsize=(15,10))
sns.boxplot(x='category', y='userId', data=df, orient="v")


# In[104]:


# checking rating for different types of item
plt.figure(figsize=(15,10))
sns.boxplot(x='category', y='rating', data=df, orient="v")


# In[115]:


# checking rating for different types of item given by user
plt.figure(figsize=(20,15))
sns.boxplot(x='userId', y='rating', data=df, orient="v")


# In[ ]:




