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
df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')  # Convert date column to datetime
st.title("🌦 London Weather Dashboard")
st.write("This dashboard analyzes and visualizes London weather data.")

print(df.columns)
print(df.head())
st.write(df.head())

st.subheader("Dataset Overview")
st.write(df.head())  # Displays the first few rows of the dataset

# Show dataset statistics
st.subheader("Dataset Statistics")
st.write(df.describe())

# Handle missing values
df["temp_max"].fillna(df["temp_max"].mean(), inplace=True)
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


st.subheader("💨 Wind Speed Distribution")

fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(df["wind"], bins=20, kde=True, ax=ax, color="green")
ax.set_xlabel("Wind Speed (km/h)")
ax.set_ylabel("Frequency")
ax.set_title("Distribution of Wind Speed")
st.pyplot(fig)

st.subheader("📈 Temperature Trends")

fig, ax = plt.subplots(figsize=(10, 5))
df["date"] = pd.to_datetime(df["date"])  # Ensure date column is in datetime format
df_sorted = df.sort_values("date")  # Sort by date
ax.plot(df_sorted["date"], df_sorted["temp_max"], label="Max Temp (°C)", color="red")
ax.plot(df_sorted["date"], df_sorted["temp_min"], label="Min Temp (°C)", color="blue")
ax.set_xlabel("Date")
ax.set_ylabel("Temperature (°C)")
ax.set_title("Max and Min Temperatures Over Time")
ax.legend()
st.pyplot(fig)



