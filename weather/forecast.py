import requests
import pandas as pd
from datetime import datetime, timezone

# Function to get 5-day weather forecast for a city
def get_forecast_by_coordinates(lat, lon, api_key, units="metric"):
    forecast_url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key,
        "units": units  # 'metric' for Celsius, 'imperial' for Fahrenheit
    }

    response = requests.get(forecast_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching forecast data: {response.status_code}")
        return None


# Process forecast data into a pandas DataFrame
def process_forecast_data(forecast_data):
    forecast_list = forecast_data['list']
    forecast_processed = []

    for item in forecast_list:
        dt = datetime.fromtimestamp(item['dt'], tz=timezone.utc)
        temp = item['main']['temp']
        forecast_processed.append({
            'datetime': dt,
            'temp': temp
        })

    df = pd.DataFrame(forecast_processed)
    return df
