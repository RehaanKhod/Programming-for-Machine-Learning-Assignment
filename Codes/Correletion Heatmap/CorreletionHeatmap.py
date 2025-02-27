# Correlation heatmap - to identify which variables influence each other the most
correlation_matrix = df_numeric.corr()  # choose only numeric columns 
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Feature Correlation Heatmap")
plt.show()
