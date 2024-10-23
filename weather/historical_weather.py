import requests  # 'requests' is used to make HTTP requests to external services (like APIs).

# --- Task: Fetching historical weather data from OpenWeatherMap API ---

def get_historical_weather(lat, lon, start, end, api_key, units="metric"):  # This function retrieves historical weather data for a given location.
    history_url = "https://history.openweathermap.org/data/2.5/history/city"  # The URL endpoint to access the OpenWeatherMap historical weather API.
    params = {  # Defining the query parameters for the API request.
        "lat": lat,  # 'lat' specifies the latitude of the location.
        "lon": lon,  # 'lon' specifies the longitude of the location.
        "type": "hour",  # 'type' determines the granularity of the data (hourly data in this case).
        "start": start,  # 'start' is the Unix timestamp representing the start time for the historical data.
        "end": end,  # 'end' is the Unix timestamp representing the end time for the historical data.
        "appid": api_key,  # 'appid' is the API key required to authenticate with the OpenWeatherMap API.
        "units": units  # 'units' determines whether the temperature is returned in metric (Celsius) or imperial (Fahrenheit).
    }

    response = requests.get(history_url, params=params)  # Makes an HTTP GET request to the API with the defined parameters.
    if response.status_code == 200:  # Checks if the API request was successful (status code 200 means OK).
        return response.json()  # If successful, returns the API response in JSON format.
    else:  # If the request failed...
        print(f"Error fetching historical weather data: {response.status_code}")  # Prints an error message indicating the failure.
        return None  # Returns None if the API request was unsuccessful.


# --- Task: Processing historical weather data into a structured format ---

def process_historical_weather_data(weather_data):  # This function processes the raw historical weather data.
    processed_data = []  # Initializes an empty list to store the processed data.

    for item in weather_data['list']:  # Loops through each item in the 'list' of weather data.
        from datetime import datetime  # Importing datetime to handle date and time conversion.

        dt = datetime.utcfromtimestamp(item['dt']).strftime('%Y-%m-%d %H:%M:%S')  # Converts the Unix timestamp ('dt') to a formatted date and time.

        temp = item['main']['temp']  # Extracts the main temperature ('temp') for this time period.
        temp_min = item['main']['temp_min']  # Extracts the minimum temperature ('temp_min') for this time period.
        temp_max = item['main']['temp_max']  # Extracts the maximum temperature ('temp_max') for this time period.

        # Appends a dictionary with the processed data (datetime, temp, min temp, max temp) to the list.
        processed_data.append({
            'datetime': dt,  # Stores the formatted date and time.
            'temp': temp,  # Stores the average temperature.
            'temp_min': temp_min,  # Stores the minimum temperature.
            'temp_max': temp_max  # Stores the maximum temperature.
        })

    import pandas as pd  # Importing pandas to structure the processed data into a DataFrame.
    df = pd.DataFrame(processed_data)  # Converts the processed data into a pandas DataFrame.
    return df  # Returns the DataFrame containing the processed historical weather data.
