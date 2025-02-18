import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

st.title("London Weather Analysis")

@st.cache_data
def load_data():
    df = pd.read_csv("London_Weather.csv")
    return df

df = load_data()
st.title("🌦 London Weather Dashboard")
st.write("This dashboard analyzes and visualizes London weather data.")

st.subheader("Dataset Overview")
st.write(df.head())  # Displays the first few rows of the dataset

df.columns = df.columns.str.strip().str.lower()  # Remove spaces and convert to lowercase
st.write("Updated Columns:", df.columns.tolist())

# Handle missing values
df["tempmax"].fillna(df["tempmax"].mean(), inplace=True)
df["wind"].fillna(df["wind"].mean(), inplace=True)
df.dropna(subset=["weather"], inplace=True)  # Only drop rows where 'weather' is missing

# Remove duplicates
df.drop_duplicates(inplace=True)

st.success("✅ Data cleaned successfully!")

st.subheader("Filter Data")
weather_options = df["weather"].unique()
selected_weather = st.selectbox("Select Weather Condition:", weather_options)
filtered_df = df[df["weather"] == selected_weather]
st.write(filtered_df)


st.subheader("📈 Temperature Trends")

fig, ax = plt.subplots(figsize=(10, 5))
df["date"] = pd.to_datetime(df["date"])  # Ensure date column is in datetime format
df_sorted = df.sort_values("date")  # Sort by date
ax.plot(df_sorted["date"], df_sorted["tempmax"], label="Max Temp (°C)", color="red")
ax.plot(df_sorted["date"], df_sorted["tempmin"], label="Min Temp (°C)", color="blue")
ax.set_xlabel("Date")
ax.set_ylabel("Temperature (°C)")
ax.set_title("Max and Min Temperatures Over Time")
ax.legend()
st.pyplot(fig)


st.subheader("💨 Wind Speed Distribution")

fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(df["wind"], bins=20, kde=True, ax=ax, color="green")
ax.set_xlabel("Wind Speed (km/h)")
ax.set_ylabel("Frequency")
ax.set_title("Distribution of Wind Speed")
st.pyplot(fig)


st.subheader("🧠 Machine Learning: Weather Prediction")

# Convert categorical weather labels into numerical values
label_encoder = LabelEncoder()
df["weather_encoded"] = label_encoder.fit_transform(df["weather"])

# Select features and target variable
X = df[["tempmax", "tempmin", "wind"]]
y = df["weather_encoded"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Decision Tree Model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Model accuracy
accuracy = accuracy_score(y_test, y_pred)
st.write(f"Model Accuracy: **{accuracy:.2f}**")

# Display classification report
st.text("Classification Report:")
st.text(classification_report(y_test, y_pred))
