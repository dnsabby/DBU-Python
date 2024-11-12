# Objective: Take the code from ex5 and modify it to include the following:

# Tasks:
from generate_weather_graphs import generate_weather_graphs
import requests
import datetime
from flask import Flask, request, render_template
import matplotlib.pyplot as plt
# Obtain and process 3 additional attributes in the weather data.
# Graphically represent the additional attributes.
# Update the HTML template to display the additional attributes.

# Submission Timeline:
# Submit the code in 2 weeks.
import os
import matplotlib
matplotlib.use('Agg')  # Use the Agg backend for non-GUI rendering

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def weather():
    weather_data = None
    graph_filenames = None

    if request.method == 'POST':
        city = request.form['city']

        # Geocoding to get latitude and longitude for the city using Open-Meteo's location API
        geocoding_response = requests.get(
            f'https://geocoding-api.open-meteo.com/v1/search?name={city}')
        print("Geocoding response:", geocoding_response.status_code,
              geocoding_response.json())

        if geocoding_response.status_code == 200 and geocoding_response.json().get('results'):
            location = geocoding_response.json()['results'][0]
            latitude, longitude = location['latitude'], location['longitude']
            print("Coordinates found:", latitude,
                  longitude)  # Verify coordinates

            # Fetch weather data with additional attributes
            weather_response = requests.get(
                f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={
                    longitude}&hourly=temperature_2m,windspeed_10m,precipitation&timezone=auto'
            )

            print("Weather response:", weather_response.status_code,
                  weather_response.json())  # Check weather response

            if weather_response.status_code == 200:
                weather_data = weather_response.json()

                # Assuming generate_weather_graphs is a function in your code
                # that takes weather_data and returns graph filenames
                graph_filenames = generate_weather_graphs(weather_data)
            else:
                weather_data = {'error': 'Unable to retrieve weather data.'}
        else:
            weather_data = {'error': 'City not found'}

    return render_template('dashboard.html', weather_data=weather_data, graph_filenames=graph_filenames)


if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(debug=True)