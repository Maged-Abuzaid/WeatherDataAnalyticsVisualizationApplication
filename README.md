# Weather Dashboard Project

## Key Learnings

Throughout the development of this weather dashboard project, several key skills and concepts were reinforced and expanded upon:

1. **API Integration**:
   - Gained practical experience working with RESTful APIs, specifically the OpenWeatherMap API.
   - Implemented API requests to fetch current weather data, 5-day forecasts, and historical weather data using the `requests` library.
   - Managed API query parameters and authenticated requests securely using environment variables.

2. **Data Processing with Pandas**:
   - Utilized `pandas` to structure, manipulate, and analyze JSON data returned from the API.
   - Efficiently handled tabular data for weather insights, including filtering, aggregation, and processing large datasets.

3. **Interactive Web Application Development**:
   - Built a dynamic and responsive dashboard using **Dash** to display real-time weather data, historical weather trends, and forecasts.
   - Developed user interfaces using Dash components like `dcc.Input`, `dcc.Dropdown`, and `dcc.Graph` for interactive data selection and visualization.
   - Managed complex callback functions to ensure smooth data flow and interactivity between components.

4. **Data Visualization with Plotly**:
   - Created visually appealing and informative graphs using `Plotly` to represent time-series data for weather forecasts and historical trends.
   - Applied techniques like filling between min/max temperature curves to enhance data clarity in line charts.
   - Customized graph layouts and themes to improve the overall aesthetic and user experience.

5. **Modular Code Design**:
   - Organized the project into multiple Python files and modules for scalability and maintainability.
   - Refactored large blocks of code into smaller, reusable functions across the project.

6. **Error Handling and Debugging**:
   - Implemented robust error handling for API responses to manage edge cases such as missing data or invalid city names.
   - Debugged issues related to API requests and data processing, ensuring smooth and reliable user experiences.

7. **Version Control and Project Management**:
   - Used `git` for version control, ensuring that code changes were tracked and managed effectively throughout the project lifecycle.
   - Adhered to best practices for project organization and documentation, making the project easy to share and collaborate on.

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
