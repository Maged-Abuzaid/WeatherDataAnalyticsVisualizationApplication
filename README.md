# Weather Dashboard Project

## Overview

This project is an **interactive weather dashboard** that allows users to fetch and visualize current weather data, 5-day weather forecasts, and historical weather data for any city. It uses the OpenWeatherMap API to retrieve weather data and displays it in a user-friendly dashboard using **Dash**.

## Features

- **Current Weather**: Displays temperature, humidity, wind speed, and other weather metrics for a selected city.
- **5-Day Forecast**: Visualizes the 5-day weather forecast in a line graph for a given city.
- **Historical Weather**: Displays historical weather data (average temperature, min/max temperatures) for the last 5 days in a graph.
- **Temperature Units**: Option to switch between Celsius and Fahrenheit for weather data.

## Technologies Used

- **Python 3.11**
- **Dash**: A web framework for building analytical web applications.
- **Plotly**: Used for visualizing weather data in graphs.
- **OpenWeatherMap API**: Used to fetch current, forecast, and historical weather data.
- **Pandas**: For data processing.
- **Requests**: For making API calls.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Maged-Abuzaid/weather_dashboard_project.git
cd weather_dashboard_project
```

### 2. Install Dependencies

Make sure you have Python 3.11 installed. Install the required Python packages by running:

```bash
pip install -r requirements.txt
```

### 3. Set Up OpenWeatherMap API Key

You will need an API key from OpenWeatherMap. Sign up at OpenWeatherMap, then add your API key to your environment variables.

On Windows:
```bash
set WEATHER_API_KEY=your_api_key
```

On macOS/Linux:
```bash
export WEATHER_API_KEY=your_api_key
```

### 4. Run the Application

After setting up the environment and installing dependencies, run the Dash application by executing:

```bash
python app.py
```

### 5. Open in Browser

Open your web browser and navigate to [http://127.0.0.1:8050/](http://127.0.0.1:8050/) to view the weather dashboard.

## Project Structure

```plaintext
weather_dashboard_project/
│
├── app.py                      # Main Dash application file
├── weather/
│   ├── current_weather.py       # Contains functions to fetch and process current weather data
│   ├── forecast.py              # Contains functions to fetch and process 5-day forecast data
│   ├── historical_weather.py    # Contains functions to fetch and process historical weather data
│
├── assets/                      # Static assets (CSS, images)
│
├── README.md                    # This file
├── requirements.txt             # Python dependencies
```

## How to Use

1. **Enter a City Name**: In the input field, type the name of the city for which you want to see the weather data (e.g., London, New York).
2. **Select Temperature Unit**: Choose between Celsius and Fahrenheit.
3. **View Weather Data**:
    - The Current Weather section shows real-time weather metrics such as temperature, humidity, wind speed, and more.
    - The 5-Day Forecast section displays a graph of the upcoming weather.
    - The Historical Weather section shows a graph of past weather data for the last 5 days.

## Screenshots

- **Dashboard Overview**:
- **Current Weather Example**:
- **5-Day Forecast Graph**:

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Special thanks to [OpenWeatherMap](https://openweathermap.org/) for providing the weather data API.
- Built using the [Dash](https://dash.plotly.com/) framework by Plotly.
