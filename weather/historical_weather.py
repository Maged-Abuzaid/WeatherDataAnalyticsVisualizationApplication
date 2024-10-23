import requests
import pandas as pd
from datetime import datetime

# Function to get historical weather data using the geographic coordinates
def get_historical_weather(lat, lon, start, end, api_key, units="metric"):
    history_url = "https://history.openweathermap.org/data/2.5/history/city"
    params = {
        "lat": lat,
        "lon": lon,
        "type": "hour",  # Retrieve hourly historical data
        "start": start,
        "end": end,
        "appid": api_key,
        "units": units
    }

    response = requests.get(history_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching historical weather data: {response.status_code}")
        return None


# Process historical weather data into a pandas DataFrame
def process_historical_weather_data(weather_data):
    processed_data = []
    for item in weather_data['list']:
        dt = datetime.utcfromtimestamp(item['dt']).strftime('%Y-%m-%d %H:%M:%S')
        temp = item['main']['temp']
        processed_data.append({
            'datetime': dt,
            'temp': temp
        })

    df = pd.DataFrame(processed_data)
    return df
