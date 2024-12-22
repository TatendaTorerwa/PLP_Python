import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Error Handling for loading the dataset
try:
    # Load the Iris dataset (you can replace this with your own dataset in CSV format)
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

    # Add a 'species' column for clarity
    df['species'] = iris.target_names[iris.target]

except FileNotFoundError:
    print("The file was not found. Please check the file path.")
except pd.errors.EmptyDataError:
    print("The file is empty. Please check the file content.")
except Exception as e:
    print(f"An error occurred: {e}")

# Task 1: Load and Explore the Dataset
print("First few rows of the dataset:")
print(df.head())

# Check data types and missing values
print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

# Handle missing values (if any) - For now, let's fill missing values with the mean
df.fillna(df.mean(), inplace=True)

# Task 2: Basic Data Analysis
print("\nBasic Statistics (Numerical Columns):")
print(df.describe())

# Grouping by 'species' and computing the mean of numerical columns
grouped = df.groupby('species').mean()
print("\nAverage of numerical columns grouped by 'species':")
print(grouped)

# Task 3: Data Visualization

# 1. Line chart - Example: Trend of 'sepal length' (Simulated Time-Series)
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['sepal length (cm)'], label='Sepal Length', color='blue')
plt.title('Sepal Length Trend')
plt.xlabel('Index')
plt.ylabel('Sepal Length (cm)')
plt.legend()
plt.grid(True)
plt.show()

# 2. Bar Chart - Average petal length per species
plt.figure(figsize=(10, 6))
sns.barplot(x='species', y='petal length (cm)', data=df)
plt.title('Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')
plt.show()

# 3. Histogram - Distribution of 'sepal width'
plt.figure(figsize=(10, 6))
sns.histplot(df['sepal width (cm)'], bins=10, kde=True)
plt.title('Distribution of Sepal Width')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.show()

# 4. Scatter Plot - Sepal Length vs Petal Length
plt.figure(figsize=(10, 6))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', data=df, hue='species')
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.show()

# Save the last plot as a PNG image
plt.savefig('sepal_length_vs_petal_length.png')
