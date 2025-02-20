# Ensure date column is in datetime format
df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y', errors='coerce')
# Seasonal Trends in Temperature & Precipitation - Identify how temperature and precipitation vary across seasons
# Define seasons
df['season'] = df['date'].dt.month.map({
    12: 'Winter', 1: 'Winter', 2: 'Winter',
    3: 'Spring', 4: 'Spring', 5: 'Spring',
    6: 'Summer', 7: 'Summer', 8: 'Summer',
    9: 'Autumn', 10: 'Autumn', 11: 'Autumn'
})

# Plot seasonal temperature trends
plt.figure(figsize=(10, 6))
sns.boxplot(x=df['season'], y=df['temp_max'], palette="coolwarm")
plt.xlabel("Season")
plt.ylabel("Max Temperature (°C)")
plt.title("Max Temperature Distribution by Season")
plt.show()

# Seasonal precipitation trends
plt.figure(figsize=(10, 6))
sns.boxplot(x=df['season'], y=df['precipitation'], palette="Blues")
plt.xlabel("Season")
plt.ylabel("Precipitation (mm)")
plt.title("Precipitation Distribution by Season")
plt.show()
