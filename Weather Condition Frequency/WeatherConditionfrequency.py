# Weather condition frequency -  A bar chart depicting the count of occurrences for each weather condition.
plt.figure(figsize=(10, 6))
sns.countplot(x=df['weather'], order=df['weather'].value_counts().index, palette='coolwarm')
plt.xticks(rotation=45)
plt.title("Weather Condition Frequency")
plt.show()
