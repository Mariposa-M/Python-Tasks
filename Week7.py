# Download latest version for the dataset 
# import kagglehub
# path = kagglehub.dataset_download("uciml/iris")
# print("Path to dataset files:", path)
#%% 

# Task 1: Load and Explore the Dataset
# Choose a dataset in CSV format (for example, you can use datasets like the Iris dataset, a sales dataset, or any dataset of your choice).
# Load the dataset using pandas.
# Display the first few rows of the dataset using .head() to inspect the data.
# Explore the structure of the dataset by checking the data types and any missing values.
# Clean the dataset by either filling or dropping any missing values.

import pandas as pd 

df = pd.read_csv("Iris.csv")
print(df.head())
print("\n")

df.info()
print("\n")
# There's not any missing values to be filled
# But if there's any::
df.fillna("NA")
df.info()
print("\n")

# Checking if there's any duplicates too
df.drop_duplicates()
df.info()
print("\n")

# Task 2: Basic Data Analysis
# Compute the basic statistics of the numerical columns (e.g., mean, median, standard deviation) using .describe().
# Perform groupings on a categorical column (for example, species, region, or department) and compute the mean of a numerical column for each group.
# Identify any patterns or interesting findings from your analysis.
print(df.describe())
print("\n")

print(df.groupby("Species").mean())
print(df.groupby("Species").agg({"PetalLengthCm":'mean', "PetalWidthCm": 'mean'}))

print("\n")
print("Iris-virginica has the largest Petal length & Petal width among different species.")
print("\n")

# Task 3: Data Visualization
# Create at least four different types of visualizations:
# Line chart showing trends over time (for example, a time-series of sales data).
# Bar chart showing the comparison of a numerical value across categories (e.g., average petal length per species).
# Histogram of a numerical column to understand its distribution.
# Scatter plot to visualize the relationship between two numerical columns (e.g., sepal length vs. petal length).
# Customize your plots with titles, labels for axes, and legends where necessary.

import matplotlib.pyplot as plt

# Line Chart
df.groupby('Species')['PetalWidthCm'].mean().plot(kind='line')
plt.xlabel("Petal Width in Cm")
plt.ylabel("Species")
plt.title("Average Petal Width per Species")
plt.show()
print('\n')

# Bar Chart
df.groupby('Species')['PetalLengthCm'].mean().plot(kind='bar')
plt.xlabel("Petal Length in Cm")
plt.ylabel("Species")
plt.title("Average Petal Length per Species")
plt.show()
print('\n')

# Histogram 
plt.hist(df['PetalWidthCm'])
# plt.xlabel("Petal Width")
plt.title("Petal Width Distribution")
plt.show()
print('\n')

# Scatter Plot
plt.scatter(df['PetalLengthCm'], df['SepalLengthCm'])
plt.xlabel("Petal Length in Cm")
plt.ylabel("Sepal Length in Cm")
plt.title("Petal Length VS Sepal Length")
plt.show()
print('\n')
