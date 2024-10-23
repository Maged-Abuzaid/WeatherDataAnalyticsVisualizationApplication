import requests  # 'requests' is used for making HTTP requests to the OpenWeatherMap API.

# --- Task: Fetching city coordinates using OpenWeatherMap Geocoding API ---

def get_city_coordinates(city_name, api_key):  # This function retrieves the geographical coordinates of a city by name.
    geocode_url = "https://api.openweathermap.org/geo/1.0/direct"  # The URL endpoint to access the OpenWeatherMap Geocoding API.
    params = {  # Defining the query parameters for the API request.
        "q": city_name,  # 'q' is the query, which in this case is the name of the city.
        "limit": 1,  # Limits the number of results returned to 1 (since we only need one city's data).
        "appid": api_key  # 'appid' is the API key required for authentication with OpenWeatherMap.
    }

    response = requests.get(geocode_url, params=params)  # Makes an HTTP GET request to the API with the defined parameters.
    if response.status_code == 200:  # Checks if the API request was successful (status code 200 means OK).
        data = response.json()  # Converts the API response to JSON format.
        if data:  # If the data is not empty (i.e., the city was found)...
            return data[0]  # Returns the first result (which contains the coordinates for the city).
        else:  # If no data is found for the given city...
            print(f"No results found for city: {city_name}")  # Prints a message indicating no results.
            return None  # Returns None if no results were found.
    else:  # If the API request failed...
        print(f"Error fetching geocoding data for {city_name}: {response.status_code}")  # Prints an error message indicating the failure.
        return None  # Returns None if the API request was unsuccessful.


# --- Task: Fetching current weather data for a city ---

def get_weather_by_coordinates(lat, lon, api_key, units="metric"):  # This function retrieves the current weather for a given latitude and longitude.
    weather_url = "https://api.openweathermap.org/data/2.5/weather"  # The URL endpoint to access the OpenWeatherMap current weather API.
    params = {  # Defining the query parameters for the API request.
        "lat": lat,  # 'lat' specifies the latitude of the location.
        "lon": lon,  # 'lon' specifies the longitude of the location.
        "appid": api_key,  # 'appid' is the API key required to authenticate with the OpenWeatherMap API.
        "units": units  # 'units' determines whether the temperature is returned in metric (Celsius) or imperial (Fahrenheit).
    }

    response = requests.get(weather_url, params=params)  # Makes an HTTP GET request to the API with the defined parameters.
    if response.status_code == 200:  # Checks if the API request was successful (status code 200 means OK).
        return response.json()  # If successful, returns the API response in JSON format.
    else:  # If the request failed...
        print(f"Error fetching weather data: {response.status_code}")  # Prints an error message indicating the failure.
        return None  # Returns None if the API request was unsuccessful.


# --- Task: Processing current weather data into a structured format ---

def process_weather_data(weather_data, units="metric"):  # This function processes the raw weather data into a more usable format.
    main_data = weather_data['main']  # Extracts the 'main' section of the weather data, which contains temperature, pressure, and humidity.
    weather_desc = weather_data['weather'][0]['description']  # Extracts the description of the weather (e.g., clear, cloudy).
    wind_data = weather_data['wind']  # Extracts the wind-related data (speed, direction).
    city_name = weather_data['name']  # Retrieves the name of the city.
    country_code = weather_data['sys']['country']  # Retrieves the country code of the city.

    # Organizes the weather data into a dictionary for easier display or further processing.
    processed_data = {
        "City": [city_name],  # Stores the city name.
        "Country": [country_code],  # Stores the country code.
        "Temperature (°C)" if units == "metric" else "Temperature (°F)": [main_data['temp']],  # Stores the temperature, with units based on user selection.
        "Feels Like (°C)" if units == "metric" else "Feels Like (°F)": [main_data['feels_like']],  # Stores the 'feels like' temperature.
        "Min Temperature (°C)" if units == "metric" else "Min Temperature (°F)": [main_data['temp_min']],  # Stores the minimum temperature.
        "Max Temperature (°C)" if units == "metric" else "Max Temperature (°F)": [main_data['temp_max']],  # Stores the maximum temperature.
        "Humidity (%)": [main_data['humidity']],  # Stores the humidity percentage.
        "Pressure (hPa)": [main_data['pressure']],  # Stores the atmospheric pressure.
        "Weather Description": [weather_desc],  # Stores the weather description (e.g., clear sky, rain).
        "Wind Speed (m/s)" if units == "metric" else "Wind Speed (mph)": [wind_data['speed']],  # Stores the wind speed.
    }

    import pandas as pd  # Importing pandas to structure the processed data into a DataFrame.
    df = pd.DataFrame(processed_data)  # Converts the processed weather data into a pandas DataFrame.
    return df  # Returns the DataFrame containing the processed weather data.
