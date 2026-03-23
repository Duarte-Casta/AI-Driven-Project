import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import dataset
ds = pd.read_csv("data/escs_trend.csv")
print(ds.head())

# Dataset shape
print("Dataset shape:", ds.shape)

# Dataset Info
print("Dataset Info:\n ",ds.info())

# Dataset Describe
print("Dataset Describe:\n",ds.describe())

# Missing values
missing_count = ds.isna().sum()

# Percentage of missing values
missing_percent = (missing_count / len(ds)) * 100


# Table of missing values
missing_table = pd.DataFrame({
    "Missing Count": missing_count,
    "Missing %": missing_percent.round(2)
})

print(missing_table)


# Correlation matrix of categorical Features
categorical_features = ds.select_dtypes(include=['int','float']).columns
correlation_matrix = ds[categorical_features].apply(lambda x: pd.factorize(x)[0]).corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix of Categorical Features')
plt.show()
