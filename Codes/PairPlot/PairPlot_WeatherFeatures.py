#Pair Plot: Relationships Between Weather Variables
# Selecting relevant numerical columns
numeric_features = ["temp_max", "temp_min", "precipitation", "wind"]
# Create pair plot
sns.pairplot(df[numeric_features], diag_kind="kde", markers="o", plot_kws={'alpha':0.6})
plt.suptitle("Pair Plot of Weather Features", y=1.02)
plt.show()
