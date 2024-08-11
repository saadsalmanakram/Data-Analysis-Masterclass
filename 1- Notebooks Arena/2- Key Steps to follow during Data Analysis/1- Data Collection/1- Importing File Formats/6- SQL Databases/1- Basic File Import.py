import pandas as pd
import sqlite3

# Connecting to a SQL database and reading a table
conn = sqlite3.connect('example.db')
df_sql = pd.read_sql('SELECT * FROM example_table', conn)
