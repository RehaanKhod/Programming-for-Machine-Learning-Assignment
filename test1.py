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

print(df.columns)
print(df.head())
st.write(df.head())

st.subheader("Dataset Overview")
st.write(df.head())  # Displays the first few rows of the dataset

# Show dataset statistics
st.subheader("Dataset Statistics")
st.write(df.describe())

