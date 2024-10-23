import requests
from datetime import datetime, timezone

# Function to get current weather using the geographic coordinates
def get_weather_by_coordinates(lat, lon, api_key, units="metric"):
    weather_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key,
        "units": units  # 'metric' for Celsius, 'imperial' for Fahrenheit
    }

    response = requests.get(weather_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching weather data: {response.status_code}")
        return None


# Function to process current weather data
def process_weather_data(weather_data, city):
    if weather_data:
        temp = weather_data['main']['temp']
        feels_like = weather_data['main']['feels_like']
        temp_min = weather_data['main']['temp_min']
        temp_max = weather_data['main']['temp_max']
        humidity = weather_data['main']['humidity']
        pressure = weather_data['main']['pressure']
        wind_speed = weather_data['wind']['speed']
        cloudiness = weather_data.get('clouds', {}).get('all', None)
        sunrise = datetime.fromtimestamp(weather_data['sys']['sunrise'], tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
        sunset = datetime.fromtimestamp(weather_data['sys']['sunset'], tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S')

        return [
            f"Current Weather in {city}:",
            f"Temperature: {temp}°",
            f"Feels Like: {feels_like}°",
            f"Min Temperature: {temp_min}°",
            f"Max Temperature: {temp_max}°",
            f"Humidity: {humidity}%",
            f"Pressure: {pressure} hPa",
            f"Wind Speed: {wind_speed} m/s",
            f"Cloudiness: {cloudiness}%",
            f"Sunrise (UTC): {sunrise}",
            f"Sunset (UTC): {sunset}"
        ]
    return ["No data available"]

# Function to get coordinates for a city using OpenWeatherMap's Geocoding API
def get_city_coordinates(city_name, api_key):
    geocode_url = "https://api.openweathermap.org/geo/1.0/direct"
    params = {
        "q": city_name,
        "limit": 1,
        "appid": api_key
    }

    response = requests.get(geocode_url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0]  # Return the first (and only) result
        else:
            print(f"No results found for city: {city_name}")
            return None
    else:
        print(f"Error fetching geocoding data for {city_name}: {response.status_code}")
        return None