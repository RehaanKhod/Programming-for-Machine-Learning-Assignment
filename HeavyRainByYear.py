heavy_rain_df = df[df['weather'].str.lower().str.contains("heavy rain", na=False)]  # Filter only heavy rain days
heavy_rain_by_year = heavy_rain_df.groupby(df['date'].dt.year).size()  # Count occurrences per year
plt.figure(figsize=(8, 5))
heavy_rain_by_year.plot(kind='bar', color='blue', alpha=0.7)
plt.xlabel("Year")
plt.ylabel("Number of Heavy Rain Days")
plt.title("Heavy Rain Occurrences by Year")
plt.xticks(rotation=45)
plt.show()
