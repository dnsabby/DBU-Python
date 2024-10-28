# app.py
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def weather():
    weather_data = None
    if request.method == 'POST':
        city = request.form['city']
        # Geocoding to get latitude and longitude for the city using Open-Meteo's location API (or any public geocoding API)
        geocoding_response = requests.get(f'https://geocoding-api.open-meteo.com/v1/search?name={city}')
        
        if geocoding_response.status_code == 200 and geocoding_response.json().get('results'):
            location = geocoding_response.json()['results'][0]
            latitude, longitude = location['latitude'], location['longitude']
            
            # Fetch weather data for the latitude and longitude
            weather_response = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true')
            
            if weather_response.status_code == 200:
                weather_data = weather_response.json()['current_weather']
            else:
                weather_data = {'error': 'Unable to retrieve weather data.'}
        else:
            weather_data = {'error': 'City not found'}
            
    return render_template('weather.html', weather_data=weather_data)

if __name__ == '__main__':
    app.run(debug=True)