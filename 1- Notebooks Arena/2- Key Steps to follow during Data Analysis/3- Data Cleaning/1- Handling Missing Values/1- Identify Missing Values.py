# Identify missing values in each column
missing_values = df.isnull().sum()
print(missing_values)