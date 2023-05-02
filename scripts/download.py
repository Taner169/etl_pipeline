import requests
import json
import os

# API endpoint URL
url = "https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=59.9139&lon=10.7522"

# API headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# create raw directory if it doesn't exist
if not os.path.exists("data/raw"):
    os.makedirs("data/raw")

# make API request
response = requests.get(url, headers=headers)

# save response to JSON file
with open("data/raw/weather_forecast.json", "w") as f:
    json.dump(response.json(), f)
