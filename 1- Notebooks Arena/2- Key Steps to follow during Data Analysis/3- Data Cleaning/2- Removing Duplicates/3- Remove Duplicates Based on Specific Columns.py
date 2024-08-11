# Remove duplicates based on specific columns
df_no_duplicates_specific = df.drop_duplicates(subset=['column1', 'column2'])
