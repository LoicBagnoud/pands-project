import pandas as pd
import numpy as py
import matplotlib as plt

column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

df = pd.read_csv('iris.data', names=column_names)
print(df)

# Reference: ChatGPT to help out with reading data files
# Prompt - I have iris.data what file format is that?
# Chatgpt response: 
'''
The iris.data file is essentially a plain text file formatted as comma-separated values (CSV). 
Even though it doesn't have a ".csv" extension, it follows the same structure: each row represents a record, and the values are separated by commas.
'''

sepal_length = df['sepal_length']
sepal_width  = df['sepal_width']
petal_length = df['petal_length']
petal_width  = df['petal_width']
species      = df['species']

# The main issue is the presentation here I don't median displayed as 50%. Unfortunately according to the pandas documentation, percentile=[] still includes 
# the 50%. this is more of a stylistic choice but I think we need to solve it. 
df.describe(percentiles=[])

# I then went ahead and found out about select_dtypes and .agg to basically get just the numbers, seeing that we're more interested in that rather than the species at the moment. 
# and getting the aggregates of what I want. So, we first get the numeric variables only and get the aggregates of what we want.

numeric_df = df.select_dtypes(include=['number'])
summary = numeric_df.agg(['count', 'mean', 'std', 'min', 'median', 'max'])
print(summary)

# References - https://realpython.com/pandas-dataframe/#filtering-data
#              https://medium.com/@SamTaylor92/data-analysis-python-exploring-a-dataset-summary-statistics-afc7a690ec96
#              https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.select_dtypes.html
#              https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.agg.html