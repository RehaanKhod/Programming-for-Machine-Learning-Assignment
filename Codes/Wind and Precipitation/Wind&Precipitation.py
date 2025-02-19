# Wind vs precipitation - showing the relationship between wind speed and precipitation, with different weather conditions color-coded.
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df["wind"], y=df["precipitation"], hue=df["weather"], palette="coolwarm")
plt.xlabel("Wind Speed (m/s)")
plt.ylabel("Precipitation (mm)")
plt.title("Wind Speed vs Precipitation")
plt.show()
