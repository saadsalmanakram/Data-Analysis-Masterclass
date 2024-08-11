# Check if columns need type conversion (e.g., object to numeric)
df['numeric_column'] = pd.to_numeric(df['numeric_column'], errors='coerce')
