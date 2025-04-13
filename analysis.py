import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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

# The main issue is the presentation here I don't want the median displayed as 50%. Unfortunately according to the pandas documentation, percentile=[] still includes 
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
'''
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
'''
# P.S - I struggled with this because I was only getting the species to their own txt file until I realised that the reason for that
# was due to all of the above not being inside the for loop.

# Reference - https://www.w3schools.com/python/python_file_write.asp
#             https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_numeric_dtype.html

# So, for the plot I wasn't really sure how to approach. Should we get each variable only? Or maybe each variable accross all three species? After some research, 
# I found a very interesting article that showcased the different variables with all plotted on top of each other in histograms. This was what I decided to go for.

# The article used Seaborn so I went ahead and imported that.
# We first create our variables for each and we search the dataframe for their respective species lines via the loc function and check if the species
# matches the species we've chosen. 


# Next comes seaborn. I ran into several problems, particularly when it comes to the Sepal_width. 
# I discovered seaborns own built in palette and after several tries I settled with colorblind.
sns.set_palette("muted")

# After this is done, we go ahead with Seaborn itself, getting our df (dataset), our hue, which would help us know that all species need to have different colours,
# and the height which I left as the original.
# Next comes the histplot itself. We get each variable as defined, followed by the number of bins (I went with 10 after several tries) and opacity. 
petal_length_histogram = sns.FacetGrid(df, hue="species", height=3).map(sns.histplot, "petal_length", bins=10, alpha=0.5).add_legend()
petal_width_histogram = sns.FacetGrid(df, hue="species",  height=3).map(sns.histplot, "petal_width", bins=10, alpha=0.5).add_legend()
sepal_length_histogram = sns.FacetGrid(df, hue="species",  height=3).map(sns.histplot, "sepal_length", bins=10, alpha=0.5).add_legend()
sepal_width_histogram = sns.FacetGrid(df, hue="species",  height=3).map(sns.histplot, "sepal_width", bins=10, alpha=0.5).add_legend()
plt.show()
plt.close()

# Finally we saved all of the above to different pngs. ChatGPT helped me here and remminded me that the above code needed to be saved to a specific variable.
'''
ChatGPT: "The best approach is to assign each FacetGrid to a variable, save its figure immediately with the savefig method (or plt.savefig using its .fig attribute), 
and then close that figure before moving on. This ensures that each plot is saved independently without overlapping."
'''
'''
petal_length_histogram.savefig("petal_length_histogram.png", bbox_inches='tight')
petal_width_histogram.savefig("petal_width_histogram.png", bbox_inches='tight')
sepal_length_histogram.savefig("sepal_length_histogram.png", bbox_inches='tight')
sepal_width_histogram.savefig("sepal_width_histogram.png", bbox_inches='tight')
'''

# https://seaborn.pydata.org/generated/seaborn.FacetGrid.html
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html
# https://medium.com/@nirajan.acharya777/exploratory-data-analysis-of-iris-dataset-9c0df76771df
# https://matplotlib.org/stable/users/explain/colors/colors.html
# https://medium.com/@maxmarkovvision/optimal-number-of-bins-for-histograms-3d7c48086fde
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html


# Now, for the scatterplot, we need to once again decide on what colours we're going to use here. Since we've already decided on "colorblind"
# for the histograms, let's keep that one for consistency and pull from that with seaborn.
# By following the documentation inthe seaborn website, we just need to pull from our data(df), assign our x and y which have already been defined previously and choose the palette.

sepal_scatterplot = sns.scatterplot(data=df, x="sepal_length", y="sepal_width", hue="species", palette="colorblind")
plt.show()

# We repeat the same for the petals.
petal_scatterplot = sns.scatterplot(data=df, x="petal_length", y="petal_width", hue="species", palette="colorblind")
plt.show()

# One final analysis I found worth using was the pairplot. As it show cases the various relationships accross all variables, while more complete, it's also
# more overwhelming to the eyes, making minute or specific detail finding more difficult. I considered using the histogram fro the diagonal but after several 
# attepmts at trying to make it look less "squished" I eventually settled with leaving the default KDE since we're already exported the histograms anyway.

sns.pairplot(df, hue="species")
plt.show()

# https://seaborn.pydata.org/generated/seaborn.scatterplot.html
# https://seaborn.pydata.org/generated/seaborn.pairplot.html
# https://www.analyticsvidhya.com/blog/2024/02/pair-plots-in-machine-learning/