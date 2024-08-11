from mpl_toolkits.mplot3d import Axes3D

# Plot a 3D scatter plot to visualize relationships between three variables
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(df['column1'], df['column2'], df['column3'], c='r', marker='o')
ax.set_xlabel('Column1')
ax.set_ylabel('Column2')
ax.set_zlabel('Column3')
plt.title('3D Scatter Plot')
plt.show()
