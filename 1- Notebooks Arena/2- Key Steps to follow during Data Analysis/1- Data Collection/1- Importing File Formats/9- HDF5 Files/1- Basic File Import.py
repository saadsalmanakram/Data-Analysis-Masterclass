import pandas as pd

# Importing HDF5 file
df_hdf = pd.read_hdf('example.h5', key='data')
