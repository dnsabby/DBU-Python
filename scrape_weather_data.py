import requests
import json

# API URL for weather data (Berlin, for example)
api_url = 'https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m'

# Fetch data from the API
response = requests.get(api_url)

# Check if the response is successful
if response.status_code == 200:
    data = response.json()
    
    # Save the data to a JSON file for further processing
    with open("Output/weather_data.json", 'w') as f:
        json.dump(data, f, indent=4)
    
    print("Weather data fetched successfully!")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")