# Fill missing values with a specific value (e.g., 0, mean, median, mode)
df_filled_zero = df.fillna(0)
df_filled_mean = df.fillna(df.mean())
df_filled_median = df.fillna(df.median())

# Fill missing values forward (propagate last valid observation)
df_filled_ffill = df.fillna(method='ffill')

# Fill missing values backward (use next valid observation)
df_filled_bfill = df.fillna(method='bfill')
