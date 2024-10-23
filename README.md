# Weather Dashboard

## Key Learnings

During the development of this weather dashboard project, several key skills and insights were gained:

1. **API Integration**:
    - Learned how to work with RESTful APIs, specifically OpenWeatherMap, to retrieve real-time weather data, 5-day
      forecasts, and historical weather data.
    - Gained experience in securely managing API keys using environment variables and understanding the structure of API
      requests and responses.

2. **Data Processing with Pandas**:
    - Used `pandas` to efficiently structure, clean, and manipulate the weather data fetched from the API.
    - Handled complex weather data formats, including hourly and daily forecasts, to transform them into user-friendly
      formats.

3. **Interactive Web Application Development**:
    - Built an interactive and dynamic dashboard using the Dash framework, providing real-time weather updates and
      visualizations.
    - Integrated multiple interactive elements such as input fields, dropdowns, and buttons to allow users to query
      different cities and switch between Celsius and Fahrenheit.

4. **Data Visualization with Plotly**:
    - Leveraged `Plotly` to create visually appealing and informative graphs that represent temperature trends,
      including average, minimum, and maximum values.
    - Ensured clarity in visual representation through customizations like labeling, color coding, and using appropriate
      chart types for different datasets.

5. **Error Handling and Debugging**:
    - Implemented error handling for various edge cases, such as invalid city names or failed API requests.
    - Improved the app's robustness by displaying informative messages when data was missing or API calls failed.

6. **Modular Code Organization**:
    - Organized the project into separate modules for fetching and processing weather data (e.g., current weather,
      forecasts, historical data), promoting clean, maintainable code.
    - Enhanced code reusability and scalability by creating reusable functions across the project.

## Project Overview

The Weather Dashboard is an interactive application that provides users with real-time weather data, 5-day forecasts,
and historical weather analysis for any city. The dashboard allows users to query various cities and switch between
Celsius and Fahrenheit for temperature measurements. It also provides visual insights into weather trends through line
charts.

## Features

- **Current Weather**: Displays the latest weather data including temperature, humidity, wind speed, and cloud coverage.
- **5-Day Weather Forecast**: Provides an interactive line graph showing the upcoming weather trends for the selected
  city.
- **Historical Weather Analysis**: Displays past weather data for the last 5 days with minimum, maximum, and average
  temperature values.
- **Temperature Unit Toggle**: Allows users to switch between Celsius and Fahrenheit.

## Technologies Used

- **Python**: Main programming language used for developing the dashboard.
- **Dash**: Framework used for building the interactive web-based dashboard.
- **Plotly**: Library used for creating the visualizations (line charts).
- **OpenWeatherMap API**: Provides current, forecast, and historical weather data.
- **Pandas**: Used for data manipulation and analysis.
- **Requests**: For making API calls to retrieve weather data.

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

1. **Enter a City Name**: In the input field, type the name of the city for which you want to see the weather data (
   e.g., London, New York).
2. **Select Temperature Unit**: Choose between Celsius and Fahrenheit.
3. **View Weather Data**:
    - The Current Weather section shows real-time weather metrics such as temperature, humidity, wind speed, and more.
    - The 5-Day Forecast section displays a graph of the upcoming weather.
    - The Historical Weather section shows a graph of past weather data for the last 5 days.

## Contact Information

Feel free to reach out if you have any questions or suggestions:

- **Email**: [MagedM.Abuzaid@gmail.com](mailto:MagedM.Abuzaid@gmail.com)
- **LinkedIn**: [Maged Abuzaid](https://www.linkedin.com/in/magedabuzaid/)
- **GitHub**: [Maged-Abuzaid](https://github.com/Maged-Abuzaid)

## Acknowledgments

- Special thanks to [OpenWeatherMap](https://openweathermap.org/) for providing the weather data API.
- Built using the [Dash](https://dash.plotly.com/) framework by Plotly.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.