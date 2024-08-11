# Check for duplicate rows
duplicates = df.duplicated()
print(duplicates.sum())  # Number of duplicate rows
