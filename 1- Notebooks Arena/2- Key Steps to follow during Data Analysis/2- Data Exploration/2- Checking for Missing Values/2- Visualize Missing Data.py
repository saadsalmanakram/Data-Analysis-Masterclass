import seaborn as sns
import matplotlib.pyplot as plt

# Visualize missing data using a heatmap
sns.heatmap(df.isnull(), cbar=False)
plt.show()
