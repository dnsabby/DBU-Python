import matplotlib.pyplot as plt
import datetime

def generate_weather_graphs(weather_data):
    # Parse hourly data for the next 24 hours
    times = weather_data['hourly']['time'][:24]
    time_labels = [datetime.datetime.fromisoformat(time).strftime('%H:%M') for time in times]

    # Check and plot temperature if available
    if 'temperature_2m' in weather_data['hourly']:
        temperatures = weather_data['hourly']['temperature_2m'][:24]
        plt.figure(figsize=(10, 5))
        plt.plot(time_labels, temperatures, marker='o', linestyle='-', color='b')
        plt.xticks(rotation=45)
        plt.xlabel('Time (24 hours)')
        plt.ylabel('Temperature (°C)')
        plt.title('Temperature Forecast')
        plt.tight_layout()
        plt.savefig('./static/temperature_plot.png')
        plt.close()
    else:
        print("Temperature data not available")

    # Check and plot humidity if available
    if 'humidity_2m' in weather_data['hourly']:
        humidity = weather_data['hourly']['humidity_2m'][:24]
        plt.figure(figsize=(10, 5))
        plt.plot(time_labels, humidity, marker='o', linestyle='-', color='g')
        plt.xticks(rotation=45)
        plt.xlabel('Time (24 hours)')
        plt.ylabel('Humidity (%)')
        plt.title('Humidity Forecast')
        plt.tight_layout()
        plt.savefig('./static/humidity_plot.png')
        plt.close()
    else:
        print("Humidity data not available")

    # Check and plot wind speed if available
    if 'windspeed_10m' in weather_data['hourly']:
        wind_speed = weather_data['hourly']['windspeed_10m'][:24]
        plt.figure(figsize=(10, 5))
        plt.plot(time_labels, wind_speed, marker='o', linestyle='-', color='r')
        plt.xticks(rotation=45)
        plt.xlabel('Time (24 hours)')
        plt.ylabel('Wind Speed (m/s)')
        plt.title('Wind Speed Forecast')
        plt.tight_layout()
        plt.savefig('./static/wind_speed_plot.png')
        plt.close()
    else:
        print("Wind speed data not available")

    # Check and plot precipitation if available
    if 'precipitation' in weather_data['hourly']:
        precipitation = weather_data['hourly']['precipitation'][:24]
        plt.figure(figsize=(10, 5))
        plt.plot(time_labels, precipitation, marker='o', linestyle='-', color='c')
        plt.xticks(rotation=45)
        plt.xlabel('Time (24 hours)')
        plt.ylabel('Precipitation (mm)')
        plt.title('Precipitation Forecast')
        plt.tight_layout()
        plt.savefig('./static/precipitation_plot.png')
        plt.close()
    else:
        print("Precipitation data not available")

    # Return paths to all generated graphs
    return {
        'temperature': './static/temperature_plot.png' if 'temperature_2m' in weather_data['hourly'] else None,
        'humidity': './static/humidity_plot.png' if 'humidity_2m' in weather_data['hourly'] else None,
        'wind_speed': './static/wind_speed_plot.png' if 'windspeed_10m' in weather_data['hourly'] else None,
        'precipitation': './static/precipitation_plot.png' if 'precipitation' in weather_data['hourly'] else None
    }
