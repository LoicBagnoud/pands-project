# analysis.pt
# This script has thee objective of analysis the famous Iris Dataset and extracting from it valuable information about its features, their
# relationships as well as potential correlations we can find
# Author: Loic Soares Bagnoud 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

df = pd.read_csv('iris.data', names=column_names)
print(df)

sepal_length = df['sepal_length']
sepal_width  = df['sepal_width']
petal_length = df['petal_length']
petal_width  = df['petal_width']
species      = df['species']

numeric_df = df.select_dtypes(include=['number'])

with open("summary.txt", "w") as f:
    for column in numeric_df.columns:
        data = numeric_df[column].values
        
        f.write(f"Statistics for {column}:\n")
        f.write(f"  Mean: {np.mean(data):.2f}\n")
        f.write(f"  Minima: {np.min(data):.2f}\n")
        f.write(f"  Maxima: {np.max(data):.2f}\n")
        f.write(f"  Standard Deviation: {np.std(data):.2f}\n")
        f.write(f"  Median: {np.median(data):.2f}\n")
        f.write("\n")  

print("Summary exported to summary.txt")

sns.set_palette("muted")

petal_length_histogram = sns.FacetGrid(df, hue="species", height=3).map(sns.histplot, "petal_length", bins=10, alpha=0.5).add_legend()
petal_width_histogram = sns.FacetGrid(df, hue="species",  height=3).map(sns.histplot, "petal_width", bins=10, alpha=0.5).add_legend()
sepal_length_histogram = sns.FacetGrid(df, hue="species",  height=3).map(sns.histplot, "sepal_length", bins=10, alpha=0.5).add_legend()
sepal_width_histogram = sns.FacetGrid(df, hue="species",  height=3).map(sns.histplot, "sepal_width", bins=10, alpha=0.5).add_legend()
plt.show()
plt.close()

petal_length_histogram.savefig("petal_length_histogram.png", bbox_inches='tight')
petal_width_histogram.savefig("petal_width_histogram.png", bbox_inches='tight')
sepal_length_histogram.savefig("sepal_length_histogram.png", bbox_inches='tight')
sepal_width_histogram.savefig("sepal_width_histogram.png", bbox_inches='tight')

sepal_scatterplot = sns.scatterplot(data=df, x="sepal_length", y="sepal_width", hue="species", palette="colorblind")
plt.savefig("sepal_scatterplot.png", bbox_inches='tight')
plt.show()

petal_scatterplot = sns.scatterplot(data=df, x="petal_length", y="petal_width", hue="species", palette="colorblind")
plt.savefig("petal_scatterplot.png", bbox_inches='tight')
plt.show()

pair_plot = sns.pairplot(df, hue="species")
pair_plot.savefig("pairplot.png", bbox_inches='tight')
plt.show()