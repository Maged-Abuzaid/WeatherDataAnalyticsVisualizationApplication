import requests  # 'requests' is a library used for making HTTP requests to external services (like APIs).

# --- Task: Fetching 5-day forecast from OpenWeatherMap API ---

def get_forecast_by_coordinates(lat, lon, api_key, units="metric"):  # This function retrieves the 5-day forecast for a given latitude and longitude.
    forecast_url = "https://api.openweathermap.org/data/2.5/forecast"  # The URL endpoint to access the OpenWeatherMap 5-day forecast API.
    params = {  # Defining the query parameters for the API request.
        "lat": lat,  # 'lat' is the latitude of the location for which we're retrieving weather data.
        "lon": lon,  # 'lon' is the longitude of the location.
        "appid": api_key,  # 'appid' is the API key required for authentication with OpenWeatherMap.
        "units": units  # 'units' determines whether the temperature is returned in metric (Celsius) or imperial (Fahrenheit).
    }

    response = requests.get(forecast_url, params=params)  # Makes an HTTP GET request to the API with the defined parameters.
    if response.status_code == 200:  # Checks if the API request was successful (status code 200 means OK).
        return response.json()  # If successful, returns the API response in JSON format.
    else:  # If the request failed (status code is not 200)...
        print(f"Error fetching forecast data: {response.status_code}")  # Prints an error message indicating the failure.
        return None  # Returns None if the API request was unsuccessful.


# --- Task: Processing 5-day forecast data into a structured format ---

def process_forecast_data(forecast_data):  # This function processes the raw forecast data into a more usable format.
    forecast_list = forecast_data['list']  # 'list' is a key in the API response that contains a list of forecast entries (every 3 hours for 5 days).
    forecast_processed = []  # Initializes an empty list to store the processed forecast data.

    for item in forecast_list:  # Loops through each item in the forecast data list.
        from datetime import datetime, timezone  # Importing datetime to handle date and time conversion.

        dt = datetime.fromtimestamp(item['dt'], tz=timezone.utc)  # Converts the timestamp ('dt') to a human-readable date and time in UTC.

        temp = item['main']['temp']  # Extracts the main temperature ('temp') for this time period.
        temp_min = item['main']['temp_min']  # Extracts the minimum temperature ('temp_min') for this time period.
        temp_max = item['main']['temp_max']  # Extracts the maximum temperature ('temp_max') for this time period.

        # Appends a dictionary with the processed data (datetime, temp, min temp, max temp) to the list.
        forecast_processed.append({
            'datetime': dt,  # Stores the formatted date and time.
            'temp': temp,  # Stores the average temperature.
            'temp_min': temp_min,  # Stores the minimum temperature.
            'temp_max': temp_max  # Stores the maximum temperature.
        })

    # Converts the processed list into a pandas DataFrame for easier data handling and visualization.
    import pandas as pd  # Importing pandas to structure the processed data into a DataFrame.
    df = pd.DataFrame(forecast_processed)  # Creates a pandas DataFrame from the list of dictionaries.
    return df  # Returns the processed DataFrame containing the forecast data.
