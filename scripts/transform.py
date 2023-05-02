import json
import os

# load raw data from file
with open("data/raw/weather_forecast.json") as f:
    raw_data = json.load(f)

# extract relevant fields from raw data
date_list = []
temp_list = []
pressure_list = []
precip_list = []

for hour in raw_data["properties"]["timeseries"]:
    date_list.append(hour["time"])
    temp_list.append(hour["data"]["instant"]["details"]["air_temperature"])
    pressure_list.append(hour["data"]["instant"]["details"]["air_pressure_at_sea_level"])
    
    # check if next_1_hours key is present in dictionary
    if "next_1_hours" in hour["data"]:
        precip_list.append(hour["data"]["next_1_hours"]["details"]["precipitation_amount"])
    else:
        # set precipitation value to 0 for this hour
        precip_list.append(0)

# create harmonized JSON object
harmonized_data = {
    "date": date_list,
    "temperature": temp_list,
    "air pressure": pressure_list,
    "precipitation": precip_list
}

# create harmonized directory if it doesn't exist
if not os.path.exists("data/harmonized"):
    os.makedirs("data/harmonized")

# save harmonized data to file
with open("data/harmonized/weather_forecast.json", "w") as f:
    json.dump(harmonized_data, f)
