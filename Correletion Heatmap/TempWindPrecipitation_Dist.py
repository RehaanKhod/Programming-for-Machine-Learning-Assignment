#Box Plot: Temperature, Wind, and Precipitation Distribution - Helps detect outliers in temperature, wind, or precipitation
plt.figure(figsize=(10, 6))
sns.boxplot(data=df[["temp_max", "temp_min", "wind", "precipitation"]])
plt.title("Box Plot of Weather Features")
plt.ylabel("Value")
plt.xlabel("Features")
plt.show()
