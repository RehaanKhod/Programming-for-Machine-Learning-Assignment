# Wind Speed Distribution Over Time
plt.figure(figsize=(10, 6))
plt.plot(df["date"], df["wind"], color="blue", alpha=0.6)
plt.xlabel("Year")
plt.ylabel("Wind Speed (m/s)")
plt.title("Wind Speed Trends Over Time")
plt.show()
