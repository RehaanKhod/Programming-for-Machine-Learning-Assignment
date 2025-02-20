# Monthly Rainfall Trends Over the Years -rainfall changes per month over multiple years
plt.figure(figsize=(10, 6))
df.groupby([df['date'].dt.year, df['date'].dt.month])['precipitation'].mean().unstack(0).plot(kind="line", cmap="coolwarm")
plt.xlabel("Month")
plt.ylabel("Average Precipitation (mm)")
plt.title("Monthly Rainfall Trends Over the Years")
plt.legend(title="Year", bbox_to_anchor=(1, 1))
plt.show()
