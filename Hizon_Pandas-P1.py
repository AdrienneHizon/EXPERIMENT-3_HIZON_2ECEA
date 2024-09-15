#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Importing numpy, pandas, and constants of math just in case for computation, mathematical analysis, and data analysis
import numpy as np
import pandas as pd
from math import *


# In[4]:


# This will read a csv file named "cars.csv" and will be stored inside the cars variable
cars = pd.read_csv('cars.csv')
cars


# In[6]:


# This will display the first 5 rows of the table
cars.head()


# In[8]:


# This will display the last 5 rows of the table
cars.tail()

