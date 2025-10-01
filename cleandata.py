import pandas as pd
import numpy as np

# Read the CSV file
df = pd.read_csv('datasheet .csv')
print(df.head())

# Check missing values
print("Missing values in each column:")
print(df.isnull().sum())

# Handling missing values properly (no inplace=True on Series)
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Salary(ind)'] = df['Salary(ind)'].fillna(df['Salary(ind)'].mean())
df['Performance Rating'] = df['Performance Rating'].fillna(df['Performance Rating'].median())

# Handle infinite values (replace with NaN, then fill only numeric columns with their means)
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.fillna(df.select_dtypes(include=['number']).mean(), inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Handle negative values (replace with median if negative)
df['Salary(ind)'] = np.where(df['Salary(ind)'] < 0, 
                             df['Salary(ind)'].median(), 
                             df['Salary(ind)'])

df['Experience'] = np.where(df['Experience'] < 0, 
                            df['Experience'].median(), 
                            df['Experience'])

# Remove outliers in Salary using 3σ rule
salary_mean = df['Salary(ind)'].mean()
salary_std = df['Salary(ind)'].std()
lower_bound = salary_mean - (3 * salary_std)
upper_bound = salary_mean + (3 * salary_std)

df = df[(df['Salary(ind)'] >= lower_bound) & (df['Salary(ind)'] <= upper_bound)]

# Save cleaned data
df.to_csv('cleaned_datasheet.csv', index=False)
print("✅ Data cleaning completed and saved to 'cleaned_datasheet.csv'")
