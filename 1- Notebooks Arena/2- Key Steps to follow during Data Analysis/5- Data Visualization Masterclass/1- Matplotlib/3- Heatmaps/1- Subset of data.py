# Generate a heatmap for a selected subset of the data
plt.imshow(df[['column1', 'column2', 'column3']].corr(), cmap='viridis', interpolation='none')
plt.colorbar()
plt.xticks(np.arange(3), ['Column1', 'Column2', 'Column3'], rotation=90)
plt.yticks(np.arange(3), ['Column1', 'Column2', 'Column3'])
plt.title('Heatmap of Selected Columns')
plt.show()
