import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report , confusion_matrix


# Load dataset
df=pd.read_csv(r'London_Weather.csv')

# ==========================
# 🔹 DATA CLEANING & PREPROCESSING
# ==========================


# Handle missing values
df['temp_max'].fillna(df['temp_max'].mean(), inplace=True)
df['wind'].fillna(df['wind'].mean(), inplace=True)
df.dropna(subset=['weather'], inplace=True)  # Only drop rows where 'weather' is missing

# Remove duplicates
df.drop_duplicates(inplace=True)

# Fix 'precipitation' column by filling missing values for heavy rain cases
heavy_rain_condition = df["weather"].str.lower().str.contains("heavy rain", na=False)
light_rain_condition = df["weather"].str.lower().str.contains("light rain", na=False)

mean_precip_heavy = df.loc[heavy_rain_condition & (df["precipitation"] > 0), "precipitation"].mean()

# Apply mean precipitation for missing values in heavy rain conditions
if df.loc[heavy_rain_condition & (df["precipitation"] == 0), "precipitation"].count() > 0:
    df.loc[heavy_rain_condition & (df["precipitation"] == 0), "precipitation"] = mean_precip_heavy

# Select only numeric columns for visualization and modeling
df_numeric = df.select_dtypes(include=['number'])


# ==========================
# 🔹 EXPLORATORY DATA ANALYSIS (EDA) & VISUALIZATIONS
# ==========================

# Display first few rows of the dataset 
print(df.head(9))

# Scatter Plot: Wind vs. Temp Max
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='wind', y='temp_max')
plt.xlabel('Wind')
plt.ylabel('Max Temperature')
plt.title('Relationship between Wind and Max Temperature')
plt.show()

# Scatter Plot: Wind vs. Temp Min
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='wind', y='temp_min')
plt.xlabel('Wind')
plt.ylabel('Min Temperature')  # Fixed incorrect label
plt.title('Relationship between Wind and Min Temperature')
plt.show()

# Precipitation vs. Temp Max
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='precipitation', y='temp_max')
plt.xlabel('Precipitation')
plt.ylabel('Max Temperature')
plt.title('Relationship between Precipitation and Max Temperature')
plt.show()

# Precipitation vs. Temp Min (Fixed label)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='precipitation', y='temp_min')
plt.xlabel('Precipitation')
plt.ylabel('Min Temperature')  # Fixed incorrect label
plt.title('Relationship between Precipitation and Min Temperature')
plt.show()

# Correlation Heatmap - Identifies relationships between numerical features
correlation_matrix = df_numeric.corr()
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Feature Correlation Heatmap")
plt.show()

# Bar Chart: Weather Condition Frequency
plt.figure(figsize=(10, 6))
sns.countplot(x=df['weather'], order=df['weather'].value_counts().index, palette='coolwarm')
plt.xticks(rotation=45)
plt.title("Weather Condition Frequency")
plt.show()

# Scatter Plot: Wind vs. Precipitation (color-coded by weather type)
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df["wind"], y=df["precipitation"], hue=df["weather"], palette="coolwarm")
plt.xlabel("Wind Speed (m/s)")
plt.ylabel("Precipitation (mm)")
plt.title("Wind Speed vs Precipitation")
plt.show()

# Time Series Plot: Max and Min Temperature Over Time
plt.figure(figsize=(10, 6))
plt.plot(df["date"], df["temp_max"], label="Max Temperature (°C)", color="red")
plt.plot(df["date"], df["temp_min"], label="Min Temperature (°C)", color="blue")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Trends Over Time")
plt.legend()
plt.show()

# Histogram: Distribution of Max and Min Temperatures
plt.figure(figsize=(10, 6))
sns.histplot(df['temp_max'], bins=20, kde=True, color='red', label="Max Temp")
sns.histplot(df['temp_min'], bins=20, kde=True, color='blue', label="Min Temp")
plt.xlabel("Temperature (°C)")
plt.ylabel("Frequency")
plt.title("Distribution of Max and Min Temperatures")
plt.legend()
plt.show()

# Boxplot: Max Temperature Distribution Across Weather Types
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x="weather", y="temp_max")
plt.xticks(rotation=45)  # Rotate labels for better readability
plt.xlabel("Weather Type")
plt.ylabel("Max Temperature (°C)")
plt.title("Max Temperature Distribution Across Weather Types")
plt.show()


#Pair Plot: Relationships Between Weather Variables
# Selecting relevant numerical columns
numeric_features = ["temp_max", "temp_min", "precipitation", "wind"]
# Create pair plot
sns.pairplot(df[numeric_features], diag_kind="kde", markers="o", plot_kws={'alpha':0.6})
plt.suptitle("Pair Plot of Weather Features", y=1.02)
plt.show()


#Box Plot: Temperature, Wind, and Precipitation Distribution - Helps detect outliers in temperature, wind, or precipitation
plt.figure(figsize=(10, 6))
sns.boxplot(data=df[["temp_max", "temp_min", "wind", "precipitation"]])
plt.title("Box Plot of Weather Features")
plt.ylabel("Value")
plt.xlabel("Features")
plt.show()


# ==========================
# 🔹 MACHINE LEARNING MODEL: DECISION TREE CLASSIFIER
# ==========================


# Encode categorical 'weather' variable into numerical labels
le = LabelEncoder()
df['weather_encoded'] = le.fit_transform(df['weather'])  # Convert weather conditions into numeric values

# Define features (X) and target variable (y)
X = df[['temp_max', 'temp_min', 'wind', 'precipitation']]  # Features
y = df['weather_encoded']  # Encoded weather labels

# Split dataset into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Data split complete. Training samples:", len(X_train), "Testing samples:", len(X_test))





# Train Decision Tree Model
clf = DecisionTreeClassifier(max_depth=5, random_state=42)  # Adding max_depth to avoid overfitting
clf.fit(X_train, y_train)

# Generate Predictions
y_pred = clf.predict(X_test)

# Model Evaluation - Accuracy Score
accuracy = accuracy_score(y_test, y_pred)
print(f"Decision Tree Model Accuracy: {accuracy:.2f}")

# Detailed Performance Report
print(classification_report(y_test, y_pred, target_names=le.classes_))


from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# Generate confusion matrix
cm = confusion_matrix(y_test, y_pred)

# Create a labeled display of the confusion matrix
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=le.classes_)
plt.figure(figsize=(8, 6))
disp.plot(cmap="Blues", values_format="d")
plt.title("Confusion Matrix - Decision Tree Classifier")
plt.show()

