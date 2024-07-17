#!/usr/bin/env python
# coding: utf-8

# In[89]:


import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()


# In[90]:


import numpy as np
set(lst) 
for i in set(lst):
    a = 'whoAmI_'+ i
    data[a] = np.where(data['whoAmI'] == i,1,0)
    
data.head() 


# In[ ]:




