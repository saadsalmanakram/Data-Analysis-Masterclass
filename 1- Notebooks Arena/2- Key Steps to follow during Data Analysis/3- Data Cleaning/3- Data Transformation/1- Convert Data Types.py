# Convert column to a different data type
df['column_name'] = df['column_name'].astype('int')
df['date_column'] = pd.to_datetime(df['date_column'])
