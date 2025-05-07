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
All of these packages come preinstalled in Python and can be imported using the _import_ function. What follows is a list of the different packages and small descriptions.
>
#### Numpy
>
[Numpy](https://numpy.org/) provides support for large, multi-dimensional arrays and matrices, along with a wide range of mathematical functions to perform operations on them efficiently. It's the foundation for many scientific and data libraries, including Pandas and scikit-learn. For more information on how to install Numpy, please see the following: https://numpy.org/install/
>
#### Pandas
>
[Pandas](https://pandas.pydata.org/docs/index.html) is a powerful and user-friendly Python library for working with structured data. It's especially well-suited for datasets, like the Iris dataset, where each column can hold different data types. With its efficient data structures and analysis tools, Pandas makes it easy to explore and manipulate data with both numerical and categorical values. For more information on how to install Pandas, please see the following: https://pandas.pydata.org/docs/getting_started/install.html
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
__Note - While Numpy is not really needed, given Pandas, I use for one specific instance, which I've found to be incredibly useful to organise the summaries into a txt file. More information on this in the Jupyter Notebook.__

## Findings

### Running the Script

Please make sure that all packages are installed and run the script as is. It should provide you with the summary of each feature as well as Pngs of each plot discussed in the analysis below. 
>
Refer to the Jupyter Notebook included for more information on how the code is being run. 

### Summarising the Data

Explanations on the analysis of the data set can also be found in the Jupyter Notebook alongside the code explanations. 