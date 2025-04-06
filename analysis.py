import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

# df.describe(percentiles=[])

# I then went ahead and found out about select_dtypes and .agg to basically get just the numbers, seeing that we're more interested in that rather than the species at the moment. 
# and getting the aggregates of what I want. So, we first get the numeric variables only and get the aggregates of what we want.

numeric_df = df.select_dtypes(include=['number'])
numeric_summary = numeric_df.agg(['count', 'mean', 'std', 'min', 'median', 'max'])

# References - https://realpython.com/pandas-dataframe/#filtering-data
#              https://medium.com/@SamTaylor92/data-analysis-python-exploring-a-dataset-summary-statistics-afc7a690ec96
#              https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.select_dtypes.html
#              https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.agg.html

# Now that this is done, we'll go ahead and create a for loop to iterate through each column and assign each variable to its
# own named summary txt.
for col in df.columns:
    file_name = f"{col}_summary.txt"

# Next, within this loop, we're going to use the is_numeric_dtype to search each column if they are numeric. This is because we have the species which are non numerical.
# This if statement will search for the numeric values and assing them to a variable using the agg function used before and if there is a string in there (species names)
# It will do the same and count their values with value_counts

    if pd.api.types.is_numeric_dtype(df[col]):
        col_summary = df[col].agg(['count', 'mean', 'std', 'min', 'median', 'max'])
    else:
        col_summary = df[col].value_counts()

# We then move to the txt generation part. We open file name as a write file and just write in there the summaries that we're organised before in the if statement.
    with open(file_name, "w") as file:
        file.write(col_summary.to_string())
    
    print(f"Summary for {col} has been written to {file_name}")

# P.S - I struggled with this because I was only getting the species to their own txt file until I realised that the reason for that
# was due to all of the above not being inside the for loop.


# Reference - https://www.w3schools.com/python/python_file_write.asp
#             https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_numeric_dtype.html