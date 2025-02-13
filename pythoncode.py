import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter
import numpy as np
df=pd.read_csv(r'C:\Users\yosher\Downloads\london.csv')
mean_temp=df["temp_max"].mean()##calculate mean temp
mean_wind=df["wind"].mean()##calculate mean wind
df['temp_max'].fillna(value=mean_temp,inplace=True)##replaces all null temp with mean temp
df['wind'].fillna(value=mean_wind,inplace=True)##replaces all null wind with mean wind
df.dropna(inplace=True)##to replace all remaining null values in WEATHER column

df.drop_duplicates(keep=False, inplace=True)##removes all duplicates
#fixing precipitaion column
heavy_rain_condition = df["weather"].str.contains("heavy rain", case=False, na=False)
light_rain_condition = df["weather"].str.contains("light rain", case=False, na=False)

mean_precip_heavy = df.loc[heavy_rain_condition & (df["precipitation"] > 0), "precipitation"].mean()


df.loc[heavy_rain_condition & (df["precipitation"] == 0), "precipitation"] = mean_precip_heavy


df_numeric = df.select_dtypes(include=['number'])##returns columns with only numeric data type to avoid error

print(df.head(9))

#plt.figure(figsize = (10, 6))
#sns.histplot(data = df, x ='wind', bins = 'auto')
#plt.xlabel('precipitation')
#plt.ylabel('')
#plt.show()


#wind and tempmax
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='wind', y='temp_max')
plt.xlabel('Wind')
plt.ylabel('Max Temperature')
plt.title('Relationship between Wind and Max Temperature')
plt.show()
#wind and tempmin
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='wind', y='temp_min')
plt.xlabel('Wind')
plt.ylabel('Max Temperature')
plt.title('Relationship between Wind and Max Temperature')
plt.show()
#precipitation and temp max
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='precipitation', y='temp_max')
plt.xlabel('precipitation')
plt.ylabel('Max Temperature')
plt.title('Relationship between precipitation and Max Temperature')
plt.show()
#precipiation and temp min
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='precipitation', y='temp_min')
plt.xlabel('Wind')
plt.ylabel('Max Temperature')
plt.title('Relationship between precipation and min Temperature')
plt.show()
