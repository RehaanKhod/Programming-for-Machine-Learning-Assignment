import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter
import numpy as np
from sklearn.preprocessing import LabelEncoder


# Load dataset
from google.colab import files
uploaded = files.upload()
df = pd.read_csv('London_Weather.csv')



#DATA CLEANING & PREPROCESSING
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



#EXPLORATORY DATA ANALYSIS (EDA) & VISUALIZATIONS
# Display first few rows of the dataset
#print(df.head(9))

# Encode categorical 'weather' variable into numerical labels
le = LabelEncoder()
df['weather_encoded'] = le.fit_transform(df['weather'])  # Convert weather conditions into numeric values

#Define features(X)and target variable (y)
X = df[['temp_max', 'temp_min', 'wind', 'precipitation']]  # Features
y = df['weather_encoded']  # Encoded weather labels

df['date'] = pd.to_datetime(df['date'], dayfirst=True)

#Extract day,month,and year into new columns
df['day'] = df['date'].dt.day
df['month'] = df['date'].dt.month
df['year']=df['date'].dt.year
# Define weather types
weather_types = ["heavy rain", "light rain", "sun", "fog", "snow"]##initialization of array for weather types.

for weather in weather_types:
    subset1 = df[df['weather'].str.lower().str.contains(weather, na=False)]##this creates subset1 which captures all the weather types in array "weather_types"
    counts1 = subset1.groupby('year').size()  ##this counts the number of occurences of said weather events over the years
    print(f"\n{weather.title()} Days by year:")##this can be removed 
    print(counts1)
    if weather == "sun":
        color = 'gold'
        title = "Sunny Days by year"

    elif weather == "heavy rain":
        color = 'navy'
        title = "Heavy Rain Days by year"
    elif weather == "light rain":
        color = 'cyan'
    elif weather == "foggy":
        color = 'slategray'
        title = "foggy Days by year"
    elif weather == "snow":
        color = 'dodgerblue'
        title = "snow Days by year"

for weather in weather_types:
    subset2 = df[df['weather'].str.lower().str.contains(weather, na=False)]##similar to subset 1 capture all the weather types in array "weather_types"
    counts2 = subset2.groupby('month').size() ##counts the number of occurences of said weather events over the months
    print(f"\n{weather.title()} Days by month:")##can be removed only to check
    print(counts2)
    if weather == "sun":
        color = 'gold'
        title = "Sunny days by month"
        

#example of plotting a graph by month and condition "sun"
#any graph can be plotted withing the if statements and larger for statements to match both cases
        plt.figure(figsize=(8, 4))
        counts2.plot(kind='bar', color='gold', alpha=0.7)
        plt.title(title)
        plt.xlabel("month")
        plt.ylabel("Count")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    elif weather == "heavy rain":
        color = 'navy'
        title = "Heavy Rain Days by month"
    elif weather == "light rain":
        color = 'cyan'
    elif weather == "foggy":
        color = 'slategray'
        title = "foggy Days by month"
    elif weather == "snow":
        color = 'dodgerblue'
        title = "snow Days by month"
for weather in weather_types:
    subset3 = df[df['weather'].str.lower().str.contains(weather, na=False)]##again subset3 captures all weather types in array "weather_types"
    counts3 = subset3.groupby('day').size()##counts3 counts the number of occurences of weather events over the days of all the years combined
    print(f"\n{weather.title()} Days by day:")
    print(counts3)
    if weather == "sun":
        color = 'gold'
        title = "Sunny Days by days"
    elif weather == "heavy rain":
        color = 'navy'
        title = "Heavy Rain Days by days"
    elif weather=="light rain":
        color='cyan'
        title="light rain days by days"
    elif weather=="foggy":
        color='slategray'
        title="foggy days by days"
    elif weather=="snow":
        color='dodgerblue'
        title="snowy days by days"
