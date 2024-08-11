import pandas as pd
import requests

# Fetching data from an API
response = requests.get('https://api.example.com/data')
data = response.json()
df_api = pd.DataFrame(data)
