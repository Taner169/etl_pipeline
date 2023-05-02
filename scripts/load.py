import sqlite3
import pandas as pd
import json
import os

# load harmonized data from file
with open("data/harmonized/weather_forecast.json") as f:
    harmonized_data = json.load(f)

# create Pandas data table
df = pd.DataFrame(harmonized_data)

# create staged directory if it doesn't exist
if not os.path.exists("data/staged"):
    os.makedirs("data/staged")

# create SQLite database and table
conn = sqlite3.connect("data/staged/weather.db")
df.to_sql("forecast", conn, if_exists="replace", index=False)

# close database connection
conn.close()
