"""
Created on Tue May  3 15:15:14 2022
@author: GRACE ESTRADA
"""

# to do: add user input for data path
#        add outlier count
#        add mode for categorical data
#        add correlation matrix

# import libraries
import pandas as pd

# create a DataFrame using the csv data
df = pd.read_json(r'rain.json')

# display data frame
print('Data Frame: ')
print(df.head(), '\n')

# print rows before dropping
print(f'Rows: {df.shape[0]}')
print(f'Columns: {df.shape[1]}\n')

# print missing values
print(f'Missing Values: \n{df.isnull().sum()}\n')

# remove the rows with the missing values
dfclean = df.dropna()

print('Data Frame with no missing values: ')
print(f'Rows: {dfclean.shape[0]}')
print(f'Columns: {dfclean.shape[1]}\n')

# compute for the mean
print(f'Mean: \n{dfclean.mean(numeric_only=True)} \n')

# compute for the median
print(f'Median: \n{dfclean.median(numeric_only=True)} \n')

# compute for the standard deviation
print(f'Standard Deviation: \n{dfclean.std(numeric_only=True)} \n')

# END
input('\nPress ENTER to exit')