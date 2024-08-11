import matplotlib.pyplot as plt

# Plot a histogram to understand the distribution of a variable
plt.hist(df['column_name'], bins=20, edgecolor='black')
plt.title('Histogram of Column Name')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
