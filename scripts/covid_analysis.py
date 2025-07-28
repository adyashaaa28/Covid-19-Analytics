import pandas as pd
import os
import matplotlib.pyplot as plt

# Define path to the dataset
data_path = "data/covid_19_data.csv"

# Load CSV
df = pd.read_csv(data_path)

# ✅ Quick check
print("✅ CSV Loaded Successfully!\n")
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print("\nSample Data:\n", df.head())
print("\nSummary Statistics:\n", df.describe())
print("\nMissing Values:\n", df.isnull().sum())
top_countries = df.groupby('Country/Region')['Confirmed'].sum().sort_values(ascending=False).head(10)
print("\nTop 10 countries by confirmed cases:\n", top_countries)
df['ObservationDate'] = pd.to_datetime(df['ObservationDate'])
daily_trend = df.groupby('ObservationDate')['Confirmed'].sum()
print("\nDaily Trend of Confirmed Cases:\n", daily_trend.tail())

# Fix: Get last known data per country
latest_df = df[df['ObservationDate'] == df['ObservationDate'].max()]
top_10_countries = latest_df.groupby('Country/Region')['Confirmed'].sum().sort_values(ascending=False).head(10)

print("\n📌 Top 10 Countries (Final Snapshot):")
print(top_10_countries)

daily_cases = df.groupby('ObservationDate')['Confirmed'].sum()

plt.figure(figsize=(12,6))
plt.plot(daily_cases.index, daily_cases.values, marker='o')
plt.xticks(rotation=45)
plt.title('Global Daily Trend of Confirmed COVID-19 Cases')
plt.xlabel('Date')
plt.ylabel('Confirmed Cases')
plt.tight_layout()
plt.grid(True)
plt.savefig('outputs/global_daily_trend.png')  # if you want to save
plt.show()

top_10_countries.to_csv('data/top_10_countries.csv')
# Save cleaned data for Power BI
df.to_csv('data/cleaned_covid_data.csv', index=False)


