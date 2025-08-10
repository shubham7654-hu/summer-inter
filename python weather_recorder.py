import pandas as pd
from datetime import datetime

# Global storage
weather_data = []  # list of dicts: {"Date": ..., "Temperature": ..., "Condition": ...}
dates_set = set()  # to store unique dates

# Function to validate date format
def validate_date(date_str):
  try:
    datetime.strptime(date_str, "%Y-%m-%d")
    return True
  except ValueError:
    return False

# Function to add weather data
def add_weather_data():
  date = input("Enter date (YYYY-MM-DD): ").strip()
  if not validate_date(date):
    print("❌ Invalid date format! Please use YYYY-MM-DD.")
    return
  if date in dates_set:
    print("⚠ Data for this date already exists! Skipping...")
    return
  
  try:
    temperature = float(input("Enter temperature (°C): ").strip())
  except ValueError:
    print("❌ Invalid temperature! Please enter a number.")
    return
  
  condition = input("Enter weather condition (e.g., Sunny, Rainy): ").strip()
  
  # Add to list & set
  weather_data.append({
    "Date": date,
    "Temperature": temperature,
    "Condition": condition
  })
  dates_set.add(date)
  print("✅ Data added successfully!")

# Function to view weather data
def view_weather_data():
  if not weather_data:
    print("📭 No data available.")
    return
  df = pd.DataFrame(weather_data)
  print("\n📊 Recorded Weather Data:")
  print(df)

# Function to summarize trends using pandas
def summarize_data():
  if not weather_data:
    print("📭 No data available for summary.")
    return
  df = pd.DataFrame(weather_data)
  avg_temp = df["Temperature"].mean()
  print(f"🌡 Average Temperature: {avg_temp:.2f}°C")
  print("\nCondition counts:")
  print(df["Condition"].value_counts())

# Function to export data to CSV
def export_to_csv():
  if not weather_data:
    print("📭 No data available to export.")
    return
  df = pd.DataFrame(weather_data)
  df.to_csv("weather_data.csv", index=False)
  print("💾 Data exported to weather_data.csv")

# Main program loop
while True:
  print("\n===== AgriWeather Insights =====")
  print("1. Add Weather Data")
  print("2. View Weather Data")
  print("3. Summarize Data")
  print("4. Export to CSV")
  print("5. Exit")
  
  choice = input("Enter choice: ").strip()
  if choice == "1":
    add_weather_data()
  elif choice == "2":
    view_weather_data()
  elif choice == "3":
    summarize_data()
  elif choice == "4":
    export_to_csv()
  elif choice == "5":
    print("👋 Exiting program...")
    break
  else:
    print("❌ Invalid choice! Please try again.")