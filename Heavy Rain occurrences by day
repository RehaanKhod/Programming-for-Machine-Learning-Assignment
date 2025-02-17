heavy_rain_df = df[df['weather'].str.lower().str.contains("heavy rain", na=False)]
heavy_rain_by_day = heavy_rain_df.groupby(df['date'].dt.day).size()  # Count occurrences per day
plt.figure(figsize=(10, 5))
heavy_rain_by_day.plot(kind='bar', color='purple', alpha=0.7)
plt.xlabel("Day of the Month")
plt.ylabel("Number of Heavy Rain Days")
plt.title("Heavy Rain Occurrences by Day")
plt.xticks(range(1, 32))  # Days 1 to 31
plt.show()
