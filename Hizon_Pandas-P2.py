#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Importing numpy, pandas, and constants of math just in case for computation, mathematical analysis, and data analysis
import numpy as np
import pandas as pd
from math import *


# In[6]:


# This will read a csv file named "cars.csv" and will be stored inside the cars variable
cars = pd.read_csv('cars.csv')
cars


# In[7]:


# In the .loc syntax, this will slice the first 5 rows and will only slice by iteration of 2 (which will fall into an add columns)
cars.loc[0:5,::2]


# In[9]:


# .loc syntax locates the car key "Model" that has a name "Mazda RX4". When found, this will display all the data that were located at that part
cars.loc[0:5,::2]


# In[12]:


# .loc syntax locates the car key "Model" that has a name "Mazda RX4". When found, this will display all the data that were located at that part
cars.loc[cars['Model'] == 'Mazda RX4']


# In[14]:


# On the second initialization after the comma, this will only display the needed data that were provided by the instruction which is cyl and gear
cars.loc[cars['Model'] == 'Camaro Z28',['Model','cyl']]


# In[16]:


# This .loc uses multiple or statements that corresponds to a specific car model in which displays there cylinders and gears
cars.loc[(cars['Model'] == 'Mazda RX4 Wag') |
         (cars['Model'] == 'Ford Pantera L')|
         (cars['Model'] == 'Honda Civic') ,['Model','cyl','gear']]

