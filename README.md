# Programming Assignment 3: Python Data Analysis (PANDAS)
> [!NOTE]
> 💡 As an open-source software library built on top of Python specifically for data manipulation and analysis, Pandas offers data structure and operations for  powerful, flexible, and easy-to-use data analysis and manipulation.
> Learn more here at [NVIDIA Pandas](https://www.nvidia.com/en-us/glossary/pandas-python/)

## 📖 Intended Learning Outcomes
1. To identify the codes and functions incorporated in the Pandas library
2. To be able to apply and use the different codes and functions in creating a Python program using a
Pandas library

## ❓ Instructions and Problems
Write a Python script/code in the Jupyter Notebook to do the given problems. You may submit your Jupyter
notebook in the dedicated submission bin.

> [!IMPORTANT]
> For this programming assignment, download the following file and save to your default user folder: http://bit.ly/Cars_file

### 🔧 Problem 1: Heads and Tails Functionality
> [!IMPORTANT]
> Save your file as Surname_Pandas-P1.py

Using knowledge obtained from the experiment and demonstrations:

a. Load the corresponding **.csv file** into a data frame named cars using pandas 

b. Display the **first five** and **last five** rows of the resulting cars.

### 🔧 Problem 2: DataFrame Indexing and Slicing
> [!IMPORTANT]
> Save your file as Surname_Pandas-P2.py

Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and
indexing operations.

a. Display the **first five rows** with odd-numbered columns **(columns 1, 3, 5, 7...)** of cars.

b. Display the row that contains the **‘Model’** of **‘Mazda RX4’**.

c. How many **cylinders (‘cyl’)** does the car model **‘Camaro Z28’** have?

d. Determine how many **cylinders (‘cyl’)** and what **gear type (‘gear’)** do the car models **‘Mazda RX4 Wag’**, **‘Ford Pantera L’** and **‘Honda Civic’** have.

## 💿 Utilized IDE
> [!NOTE]
> Jupyter Notebook is used to solve the problem. You can use this IDE using [Anaconda Navigator](https://www.anaconda.com)

## 💻 Code Summary and Outcome

It is essential to import these libraries to ensure no ambigious syntaxes that are going to be executed in the program
```python
import numpy as np
import pandas as pd
from math import *
```

After downloading the cars.csv file, the dataframe will be put inside the "car" variable
> [!NOTE]
> The cars.csv can be downloaded inside this [link](http://bit.ly/Cars_file)

```python
cars = pd.read_csv('cars.csv')
cars
```

The result will be displayed as:

![image](https://github.com/user-attachments/assets/12a8950d-bdfc-4450-9c44-02b9e8fef4df)

### 📚 Problem 1 Solution:
To display the first five rows of this data frame, the function .head() is going to be used

```python
cars.head()
```

The result will be displayed as:

![image](https://github.com/user-attachments/assets/b90679e6-c0bc-443d-8fc8-71208e72326c)

To display the last five rows of this data frame, the function .head() is going to be used

```python
cars.tail()
```
The result will be displayed as:

![image](https://github.com/user-attachments/assets/c2a68fde-139e-4d1e-8ca9-dcf281c2e78c)


### 📚 Problem 2 Solution:
To display the first five rows with only odd-numbered columns are present, slicing will be used inside the .loc() function of the dataframe wherein the first initialization (before comma) it will only show from index 0 to 4 and in the 
second initialization (after comma) it will only slice at an iteration of 2 starting from the first index, meaning it will filter out even-numbered columns
```python
cars.loc[0:4,::2]
```

The result will be displayed as:

![image](https://github.com/user-attachments/assets/3b03d416-9d62-4211-8e80-a2a0dec1bf61)

To display a specific row wherein the details of "Mazda RX4" is present, .loc() function will still be used but this time, the key 'Model' of the dataframe will be extracted

```python
cars.loc[cars['Model'] == 'Mazda RX4']
```

The result will be displayed as:

![image](https://github.com/user-attachments/assets/af63fd63-9fd1-477d-bea0-b5672d8614f6)

To display how many cylinders are present inside the "Camaro Z28", .loc() function will be used but with additional condition, only the "Model" and "cyl" are going to be displayed on the screen

```python
cars.loc[cars['Model'] == 'Camaro Z28',['Model','cyl']]
```

The result will be displayed as:

![image](https://github.com/user-attachments/assets/2eeaa930-de39-436e-8644-37a7b2d93b30)

To display multiple specific models and only their "cyl" and "gear". The .loc() function will be used but with a condition OR statement inside the first initialization and a specific display of columns on the second initialization

```python
cars.loc[(cars['Model'] == 'Mazda RX4 Wag') |
         (cars['Model'] == 'Ford Pantera L')|
         (cars['Model'] == 'Honda Civic') ,['Model','cyl','gear']]
```

The result will be displayed as:

![image](https://github.com/user-attachments/assets/4e8875a7-2022-435f-9df2-ea8f62e0e3af)

With these problems that were solved, the students will be able to meet the intended learning outcome that this assignment is aiming to achieve.

## 🛠 Author
#### Name: Kyle Adrienne S. Hizon
#### Section: 2ECE-A

## 🔑 Version History

- 1.02
  - Added the supplemental files
  - Revamped the readme file

- 1.01
  - Readme file completed

- 1.00 
  - Repository has been established
