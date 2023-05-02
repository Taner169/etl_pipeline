import pandas as pd
import matplotlib.pyplot as plt

# read harmonized data from file
df = pd.read_json("data/harmonized/weather_forecast.json")

# create line chart of temperature data
plt.plot(df["date"], df["temperature"])
plt.title("Weather Forecast")
plt.xlabel("Date")
plt.ylabel("Temperature (Celsius)")
plt.show()
