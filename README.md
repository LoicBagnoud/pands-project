# *Iris* flower data set

> “if we are to learn anything about the ultimate nature of species we must reduce the problem to the simplest terms and study a few easily recognized, well differentiated species”
> 
> — **Edgar Anderson**  
> *The problem of species in the northern blue flags, Iris versicolor L. and Iris virginica L. Annals of the Missouri Botanical Garden, 1928*

This famous dataset, known to be used in R.A. Fisher's classic 1936 paper, *The Use of Multiple Measurements in Taxonomic Problems*, includes three iris species with 50 samples each as well as some properties about each flower.
>
The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor) and has been one of the earliest datasets in Statistis and Computer Science as well as in the literature on classification methods. 
> 
>
## Objective

The purpose of this project will be to extract the data and analyse it by creating a program that:
> 
1. Extracts and organises the different flower types and their categories
2. Summarises each variable to a single text file that one can then use.
3. Saves a histogram of each variable to png files, and outputs a scatter plot of each pair of variables. 
4. Outputs a Pairplot between the different species' variables.
5. Extracts a possible correlation between the various species. 

## Table of Contents
- [Packages needed](#Packages-needed)
    - [Numpy](#Numpy)
    - [Pandas](#Pandas)
    - [Seaborn](#Seaborn)
    - [Matplotlib](#Matplotlib)
- [Findings](#Findings)
    - [Running the Script](#Running-the-Script)
    - [Summarising the Data](#Summarising-the-Data)
- [References](#References)

## Packages needed

To run this project, you'll need Python 3 installed on your machine. You can download the latest version from the official Python website: https://www.python.org/downloads/
>
Please make sure you follow the instructions outlined there. Additionally, this code uses several packages in order to achieve most of the tasks' objectives. It is expected that those are also properly downloaded and installed on your machine.
>
Instrutions are provided in each package below in order to install them but it is advisable to use Anaconda Distribution as it already contains these packages pre-installed. You can download Anaconda Distribution from here: https://www.anaconda.com/download/success

All of the packages required are as follows:
>
- Matplotlib
- Numpy
- Pandas
- Seaborn
>
All of these packages can be imported using the _import_ function. What follows is a list of the different packages and small descriptions alongside links on how to download them and install if you prefer not to use Anaconda Distribution.
>
#### Numpy
>
[Numpy](https://numpy.org/) provides support for large, multi-dimensional arrays and matrices, along with a wide range of mathematical functions to perform operations on them efficiently. It's the foundation for many scientific and data libraries, including Pandas and scikit-learn. For more information on how to install Numpy, please see the following: https://numpy.org/install/
>
#### Pandas
>
[Pandas](https://pandas.pydata.org/docs/index.html) is a powerful and user-friendly Python library for working with structured data. It's especially well-suited for datasets, like the Iris dataset, where each column can hold different data types. With its efficient data structures and analysis tools, Pandas makes it easy to explore and manipulate data with both numerical and categorical values. For more information on how to install Pandas, please see the following: https://pandas.pydata.org/docs/getting_started/install.html
>
#### Matplotlib
>
[Matplotlib](https://matplotlib.org/) is an especially useful package for plotting data in formats like line charts, bar graphs, scatter plots, and more. For more information installing matplotlib, please see the following: https://matplotlib.org/stable/users/getting_started/
>
#### Seaborn
>
As per their website, [Seaborn](https://seaborn.pydata.org/) is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics. For more information installing matplotlib, please see the following: https://seaborn.pydata.org/installing.html

>
For more help in understanding and dealing with each package, please make sure to review and investigate the relevant documentation if anything remains unclear:
>
- [Numpy Documentation](https://numpy.org/doc/stable/)
- [Pandas Documentation](https://pandas.pydata.org/docs/index.html)
- [Matplotlib Documentation](https://matplotlib.org/)
- [Seaborn Documentation](https://seaborn.pydata.org/)
>
__Note - While Numpy is not really needed, given Pandas, I will use it for one specific instance, which I've found to be incredibly useful to organise the summaries into a txt file. More information on this in the Jupyter Notebook.__

## Findings

### Running the Script

Please make sure that all packages are installed and run the script as is. It should provide you with the summary of each feature as well as Pngs of each plot discussed in the analysis below. The repository also already contains the relevant pngs and txt file in their appropriate folder. Additionally, two data files are in there: iris.names and iris.data.
>
These are essential as they are the raw Iris data taken from [UC Irvine](https://archive.ics.uci.edu/dataset/53/iris). 
>
Refer to the Jupyter Notebook included for more information on how the code is being run and choices made there.

### Summarising the Data

Explanations on the analysis of the data set can also be found in the Jupyter Notebook alongside the code explanations. I found it more useful and organised to have everything in one single Jupyter Notebook, rather than in the Readme file.
>
Below, you'll also find a list of references. These have also been included in the Jupyter Notebooks since superscript reference numbers are used to indicate where each reference was used.

### References

- ChatGPT. (2025) __Response__: *The iris.data file is essentially a plain text file formatted as comma-separated values (CSV). Even though it doesn't have a ".csv" extension, it follows the same structure: each row represents a record, and the values are separated by commas.* OpenAI. Available at: https://chat.openai.com/ 

- Taylor, S. (2019) Data Analysis Python: Exploring a Dataset & Summary Statistics. Medium. Available at: https://medium.com/@SamTaylor92/data-analysis-python-exploring-a-dataset-summary-statistics-afc7a690ec96 

-  Real Python. (n.d.) Filtering Data in a DataFrame. Available at: https://realpython.com/pandas-dataframe/#filtering-data 

-  pandas. (n.d.) pandas.DataFrame.select_dtypes. Available at: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.select_dtypes.html 

-  W3Schools. (n.d.) Python File Write. Available at: https://www.w3schools.com/python/python_file_write.asp 

-  pandas. (n.d.) pandas.api.types.is_numeric_dtype. Available at: https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_numeric_dtype.html 

-  Seaborn. (n.d.) seaborn.FacetGrid. Available at: https://seaborn.pydata.org/generated/seaborn.FacetGrid.html 

-  Acharya, N. (2021) Exploratory Data Analysis of Iris Dataset. Medium. Available at: https://medium.com/@nirajan.acharya777/exploratory-data-analysis-of-iris-dataset-9c0df76771df 

-  Matplotlib. (n.d.) Colors in Matplotlib. Available at: https://matplotlib.org/stable/users/explain/colors/colors.html 

-  Seaborn. (n.d.) Color Palettes. Available at: https://seaborn.pydata.org/tutorial/color_palettes.html 

-  Seaborn. (n.d.) seaborn.color_palette. Available at: https://seaborn.pydata.org/generated/seaborn.color_palette.html 

-  Markov, M. (2021) Optimal Number of Bins for Histograms. Medium. Available at: https://medium.com/@maxmarkovvision/optimal-number-of-bins-for-histograms-3d7c48086fde 

-  Matplotlib. (n.d.) matplotlib.pyplot.savefig. Available at: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html 

-  ChatGPT. (2025) __Response__: *The best approach is to assign each FacetGrid to a variable, save its figure immediately with the savefig method (or plt.savefig using its .fig attribute), and then close that figure before moving on. This ensures that each plot is saved independently without overlapping.* OpenAI. Available at: https://chat.openai.com/ 

-  Seaborn. (n.d.) seaborn.scatterplot. Available at: https://seaborn.pydata.org/generated/seaborn.scatterplot.html 

-  ChatGPT. (2025).

    __Prompt__: _Why am I getting AttributeError: 'AxesSubplot' object has no attribute 'savefig' when I try to save the scatterplot to a PNG file?_

    __Response__: _sepalscatterplot is not a full figure (Figure object); it’s an AxesSubplot object (the "area" inside the figure where the plot happens). Axes objects do not have a .savefig() method. Only the entire Figure object (controlled by matplotlib) has .savefig()! Call plt.savefig(...) after plotting, like this: plt.savefig(...)._
    OpenAI. Available at: https://chat.openai.com/ 

-  Scaler. (n.d.) NumPy polyfit: Fitting trend lines to data. Available at: https://www.scaler.com/topics/numpy-polyfit/ 

-  NumPy Developers. (n.d.) numpy.linspace — NumPy v1.26 Manual. Available at: https://numpy.org/doc/stable/reference/generated/numpy.linspace.html 

-  THAMIZH-ARASU. (n.d.) Exploratory Data Analysis on The Iris Data Set. Available at: https://github.com/THAMIZH-ARASU/Exploratory-Data-Analysis-on-The-Iris-Data-Set/blob/main/iris_exploration.ipynb 

-  Seaborn. (n.d.) seaborn.lmplot. Available at: https://seaborn.pydata.org/generated/seaborn.lmplot.html 

-  Seaborn. (n.d.) seaborn.pairplot. Available at: https://seaborn.pydata.org/generated/seaborn.pairplot.html 

-  Fisher, R.A. (1936) The use of multiple measurements in taxonomic problems. Annals of Eugenics, 7(2), pp.179–188. Available at: https://onlinelibrary.wiley.com/doi/10.1111/j.1469-1809.1936.tb02137.x 

-  Analytics Vidhya. (2024) Pair Plots in Machine Learning. Available at: https://www.analyticsvidhya.com/blog/2024/02/pair-plots-in-machine-learning/ 