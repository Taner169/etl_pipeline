import json
import os

# load harmonized data from file
with open("data/harmonized/weather_forecast.json") as f:
    harmonized_data = json.load(f)

# remove duplicates from data
cleaned_data = {}
cleaned_data["date"] = list(set(harmonized_data["date"]))
cleaned_data["temperature"] = [harmonized_data["temperature"][harmonized_data["date"].index(date)] for date in cleaned_data["date"]]
cleaned_data["air pressure"] = [harmonized_data["air pressure"][harmonized_data["date"].index(date)] for date in cleaned_data["date"]]
cleaned_data["precipitation"] = [harmonized_data["precipitation"][harmonized_data["date"].index(date)] for date in cleaned_data["date"]]

# create cleansed directory if it doesn't exist
if not os.path.exists("data/cleansed"):
    os.makedirs("data/cleansed")

# save cleaned data to file
with open("data/cleansed/weather_forecast.json", "w") as f:
    json.dump(cleaned_data, f)
