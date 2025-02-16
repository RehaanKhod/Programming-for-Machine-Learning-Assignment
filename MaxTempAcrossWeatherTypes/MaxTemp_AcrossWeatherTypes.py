# Max Temperature Across Weather Types - Shows the temperature range for different weather conditions & detect outliers(ex:  unusually high/low temps)
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x="weather", y="temp_max")
plt.xticks(rotation=45)  # Rotate labels for better readability
plt.xlabel("Weather Type")
plt.ylabel("Max Temperature (°C)")
plt.title("Max Temperature Distribution Across Weather Types")
plt.show()
