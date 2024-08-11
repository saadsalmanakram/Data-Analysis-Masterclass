duplicates = df_csv.duplicated().sum()
print(f"Number of duplicate rows: {duplicates}")
