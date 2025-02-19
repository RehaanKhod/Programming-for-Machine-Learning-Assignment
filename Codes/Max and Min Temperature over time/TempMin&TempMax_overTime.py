# Temp Min and Temp Max over time - A time-series line plot displaying max and min temperatures over several years
plt.figure(figsize=(10, 6))
plt.plot(df["date"], df["temp_max"], label="Max Temperature (°C)", color="red")
plt.plot(df["date"], df["temp_min"], label="Min Temperature (°C)", color="blue")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Trends Over Time")
plt.legend()
plt.show()
