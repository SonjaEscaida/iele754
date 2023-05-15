#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats


# In[2]:


uniform_data = stats.uniform.rvs(size = 100000, loc = 0, scale= 10)


# In[3]:


pd.DataFrame(uniform_data).plot(kind="density", figsize=(9,9), xlim=(-1,11))


# In[4]:


stats.uniform.cdf(x=2.5, loc=0, scale=10)  #Al correrlo =0.25


# In[5]:


stats.uniform.ppf(q=0.4, loc=0, scale=10) #= 4.0


# In[30]:


for x in range(-1, 12, 3):
    print("Density as x value"+ str(x))
    print (stats.uniform.pdf(x, loc=0, scale=10))


# In[7]:


import random
random.randint(0,10)


# In[8]:


random.choice([2,4,6,9])


# In[9]:


random.random()


# In[10]:


random.uniform(0,10)


# In[11]:


random.seed(12) #Set the seed for an arbitrary value
print (random.uniform(0,10) for x in range(4))
random.seed(12) #Set the seed to the same value
print([random.uniform(0,10) for x in range(4)])


# In[12]:


prob_under_minus1 = stats.norm.cdf(x=-1, loc=0, scale=1)
prob_over_1 = stats.norm.cdf(x=1, loc=0, scale=1) 
between_prob = 1-(prob_under_minus1 + prob_over_1)
print(prob_under_minus1, prob_over_1, between_prob)


# In[34]:


plt.rcParams["figure.figsize"] = (7, 7)
plt.fill_between(x=np.arange(-4,-1,0.01), y1= stats.norm.pdf(np.arange(-4,-1,0.01)), facecolor='red', alpha= 0.35)
plt.fill_between(x=np.arange(1,4,0.01), y1= stats.norm.pdf(np.arange(1,4,0.01)), facecolor='red', alpha= 0.35)
plt.fill_between(x=np.arange(-1,1,0.01), y1= stats.norm.pdf(np.arange(-1,1,0.01)), facecolor='blue', alpha= 0.35)
plt.text(x=-1.8,y=0.03, s=round(prob_under_minus1,3))
plt.text(x=-0.2,y=0.1, s=round(between_prob,3))
plt.text(x=1.4,y=0.03, s=round(prob_over_1,3))
("")


# In[ ]:


print(stats.norm.pdf( q=0.025))
print(stats.norm.pdf( q=0.975)) 


# In[14]:


print(stats.norm.cdf( x=-3))
print(stats.norm.cdf( x=3))


# In[15]:


fair_coin_flips = stats.binom.rvs(n=10, p=0.5, size=10000)
print(pd.crosstab(index='counts', columns= fair_coin_flips))
pd.DataFrame(fair_coin_flips).hist(range=(-0.5,10.5), bins=11)


# In[16]:


stats.binom.cdf(k=5, n=10, p=0.8)


# In[17]:


1-stats.binom.cdf(k=5, n=10, p=0.8)


# In[18]:


stats.binom.pmf(k=5, n=10, p=0.5)


# In[19]:


stats.binom.pmf(k=8, n=10, p=0.8)


# In[20]:


random.seed(12)
flips_till_heads = stats.geom.rvs(size=10000, p=0.5)
print(pd.crosstab(index='counts', columns=flips_till_heads))
pd.DataFrame(flips_till_heads).hist(range=(-0.5,max(flips_till_heads)+0.5), bins=max(flips_till_heads)+1)


# In[21]:


first_five= stats.geom.cdf(k=5, p=0.5)
1- first_five


# In[35]:


stats.geom.pmf(k=2, p=0.5)


# In[23]:


prob_1 = stats.expon.cdf(x=1, scale=1)
1- prob_1


# In[24]:


plt.fill_between(x=np.arange(0,1,0.01), y1= stats.expon.pdf(np.arange(0,1,0.01)), facecolor='blue', alpha= 0.35) 
plt.fill_between(x=np.arange(1,7,0.01), y1= stats.expon.pdf(np.arange(1,7,0.01)), facecolor='red', alpha= 0.35)  
plt.text(x=0.3,y=0.2, s=round(prob_1,3))
plt.text(x=1.5,y=0.08, s=round(1-prob_1,3))


# In[26]:


random.seed(12)
arrival_rate_1= stats.poisson.rvs(size=10000, mu=1)
print(pd.crosstab(index='counts', columns=arrival_rate_1))
pd.DataFrame(arrival_rate_1).hist(range=(-0.5,max(arrival_rate_1)+0.5), bins=max(arrival_rate_1)+1)


# In[27]:


random.seed(12)
arrival_rate_10= stats.poisson.rvs(size=10000, mu=10)
print(pd.crosstab(index='counts', columns=arrival_rate_10))
pd.DataFrame(arrival_rate_10).hist(range=(-0.5,max(arrival_rate_10)+0.5), bins=max(arrival_rate_10)+1)


# In[ ]:





# In[ ]:




