# Histogram for Max and Min Temperatures - Shows how often different temperatures occur
plt.figure(figsize=(10, 6))
sns.histplot(df['temp_max'], bins=20, kde=True, color='red', label="Max Temp")
sns.histplot(df['temp_min'], bins=20, kde=True, color='blue', label="Min Temp")
plt.xlabel("Temperature (°C)")
plt.ylabel("Frequency")
plt.title("Distribution of Max and Min Temperatures")
plt.legend()
plt.show()
