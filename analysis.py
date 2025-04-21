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
numeric_summary = numeric_df.agg(['count', 'mean', 'std', 'min', 'median', 'max'])

for col in df.columns:
    file_name = f"{col}_summary.txt"

    if pd.api.types.is_numeric_dtype(df[col]):
        col_summary = df[col].agg(['count', 'mean', 'std', 'min', 'median', 'max'])
    else:
        col_summary = df[col].value_counts()

    with open(file_name, "w") as file:
        file.write(col_summary.to_string())
    
    print(f"Summary for {col} has been written to {file_name}")

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
plt.show()

petal_scatterplot = sns.scatterplot(data=df, x="petal_length", y="petal_width", hue="species", palette="colorblind")
plt.show()

sns.pairplot(df, hue="species")
plt.show()