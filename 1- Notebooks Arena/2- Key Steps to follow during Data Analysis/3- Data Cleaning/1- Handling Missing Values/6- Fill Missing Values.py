# Fill missing values with a specific value (e.g., 0 or mean of the column)
df_filled = df.fillna(0)
df_filled = df.fillna(df.mean())
