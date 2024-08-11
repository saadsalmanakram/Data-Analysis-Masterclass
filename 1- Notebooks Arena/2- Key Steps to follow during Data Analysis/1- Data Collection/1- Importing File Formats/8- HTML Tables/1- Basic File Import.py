import pandas as pd

# Importing data from an HTML table
df_html = pd.read_html('example.html')[0]  # Reads the first table on the page
