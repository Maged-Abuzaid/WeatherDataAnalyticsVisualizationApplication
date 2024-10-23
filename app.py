import os  # The 'os' module allows interaction with the operating system, here used to retrieve environment variables.
import dash  # 'dash' is the main package used to create interactive web applications in Python.
from dash import dcc, html  # 'dcc' provides dashboard components, and 'html' allows HTML elements to be used in the app.
from dash.dependencies import Input, Output  # 'Input' and 'Output' manage how user interactions update the UI.
import plotly.express as px  # 'plotly.express' is used to easily create graphs, especially for time series data.
from datetime import datetime, timezone, timedelta  # Importing functions to manage and manipulate dates and times.

# Import custom functions from other modules to handle fetching and processing weather data.
from weather.current_weather import get_weather_by_coordinates, process_weather_data, get_city_coordinates
from weather.forecast import get_forecast_by_coordinates, process_forecast_data
from weather.historical_weather import get_historical_weather, process_historical_weather_data

# --- Task: Setting up environment variables and initializing the app ---

# Get the API key from the system environment variable
api_key = os.getenv("WEATHER_API_KEY")  # Retrieves the API key stored in the environment variable named 'WEATHER_API_KEY'.

if not api_key:  # This condition checks if the API key was retrieved successfully.
    raise ValueError("API key not found in environment variables. Make sure WEATHER_API_KEY is set.")  # Raises an error if the API key is not found.

# Initialize Dash app
app = dash.Dash(__name__)  # Initializes the Dash app instance, which serves as the main object for the app.

# --- Task: Defining the layout of the application ---

# Define the layout
app.layout = html.Div([  # The main container (a div element) that holds all the components of the app.
    html.H1("Interactive Weather Dashboard", style={'textAlign': 'center', 'padding-bottom': '20px'}),  # Creates a centered title with padding below it.

    # City input and submit button
    html.Div([  # Div container that groups the city input and submit button.
        html.Label("Enter city name for weather analysis (e.g., London):", style={'margin-right': '10px'}),  # A label prompting the user to enter a city.
        dcc.Input(id='city-input', value='London', type='text', style={'width': '300px', 'margin-right': '20px'}),  # Input field where the user can type a city name, defaulting to 'London'.
        html.Button('Submit', id='submit-button', n_clicks=0),  # A submit button that, when clicked, will trigger updates to the weather dashboard.
    ], style={'textAlign': 'center', 'padding': '20px 0'}),  # Center-aligns the input section and adds padding above and below it.

    # Temperature unit selection dropdown
    html.Div([  # A div container for the dropdown to choose between Celsius and Fahrenheit.
        html.Label("Select temperature unit:", style={'margin-right': '10px'}),  # Label describing the dropdown's purpose.
        dcc.Dropdown(  # Dropdown menu allowing the user to select a temperature unit.
            id='unit-dropdown',
            options=[  # The available options for the dropdown.
                {'label': 'Celsius (°C)', 'value': 'metric'},  # Option to choose Celsius, represented by 'metric'.
                {'label': 'Fahrenheit (°F)', 'value': 'imperial'}  # Option to choose Fahrenheit, represented by 'imperial'.
            ],
            value='metric',  # The default selection is Celsius ('metric').
            style={'width': '200px', 'margin': '0 auto'}  # The dropdown has a fixed width and is centered horizontally.
        ),
    ], style={'textAlign': 'center', 'padding': '10px 0'}),  # Centers the dropdown and adds some padding around it.

    # Container to display current weather information
    html.Div(id='current-weather-output', style={'padding': '20px', 'text-align': 'center', 'font-size': '18px'}),  # A div where the current weather data will be displayed in table form.

    # Graphs for forecast and historical weather
    dcc.Graph(id='forecast-graph'),  # This component will display the 5-day forecast as a graph.
    dcc.Graph(id='historical-weather-graph')  # This component will display the historical weather data as a graph.
])

# --- Task: Defining the callback for updating weather data and graphs ---

# Callback to update current weather, forecast graph, and historical weather graph
@app.callback(
    [Output('current-weather-output', 'children'),  # Updates the content of the 'current-weather-output' div.
     Output('forecast-graph', 'figure'),  # Updates the figure (graph) for the 'forecast-graph' component.
     Output('historical-weather-graph', 'figure')],  # Updates the figure (graph) for the 'historical-weather-graph' component.
    [Input('submit-button', 'n_clicks')],  # This callback is triggered when the submit button is clicked.
    [dash.dependencies.State('city-input', 'value'),  # Gets the current value from the 'city-input' field.
     dash.dependencies.State('unit-dropdown', 'value')]  # Gets the current value from the 'unit-dropdown' field (Celsius or Fahrenheit).
)
def update_weather_dashboard(n_clicks, city, unit_system):  # Function that updates weather data when the submit button is clicked.
    coordinates = get_city_coordinates(city, api_key)  # Retrieves the latitude and longitude of the city entered by the user.
    if coordinates:  # If coordinates are found for the given city...
        lat, lon = coordinates['lat'], coordinates['lon']  # Extracts the latitude and longitude from the coordinates.

        # Fetch and display current weather data
        weather_data = get_weather_by_coordinates(lat, lon, api_key, units=unit_system)  # Fetches current weather data using the city’s coordinates and the chosen temperature unit.
        if weather_data:  # If weather data is retrieved successfully...
            # Structure the current weather data into a table with styling
            current_weather_output = html.Table([  # Constructs an HTML table to display the weather parameters and values.
                html.Thead(html.Tr([html.Th("Weather Parameter"), html.Th("Value")]),  # Defines the table header with two columns: "Weather Parameter" and "Value".
                           style={'backgroundColor': '#4CAF50', 'color': 'white'}),  # Styles the header with a green background and white text.
                html.Tbody([  # The body of the table contains the weather data rows.
                    html.Tr([html.Td("Temperature"), html.Td(f"{weather_data['main']['temp']}°")]),  # Row displaying the temperature.
                    html.Tr([html.Td("Feels Like"), html.Td(f"{weather_data['main']['feels_like']}°")]),  # Row displaying what the temperature feels like.
                    html.Tr([html.Td("Min Temperature"), html.Td(f"{weather_data['main']['temp_min']}°")]),  # Row for the minimum temperature.
                    html.Tr([html.Td("Max Temperature"), html.Td(f"{weather_data['main']['temp_max']}°")]),  # Row for the maximum temperature.
                    html.Tr([html.Td("Humidity"), html.Td(f"{weather_data['main']['humidity']}%")]),  # Row displaying the humidity percentage.
                    html.Tr([html.Td("Pressure"), html.Td(f"{weather_data['main']['pressure']} hPa")]),  # Row showing the atmospheric pressure.
                    html.Tr([html.Td("Wind Speed"), html.Td(f"{weather_data['wind']['speed']} m/s")]),  # Row showing the wind speed.
                    html.Tr([html.Td("Cloudiness"), html.Td(f"{weather_data.get('clouds', {}).get('all', 'N/A')}%")]),  # Row showing cloudiness, if available.
                    html.Tr([html.Td("Sunrise (UTC)"), html.Td(datetime.fromtimestamp(weather_data['sys']['sunrise'], tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S'))]),  # Row for sunrise time in UTC.
                    html.Tr([html.Td("Sunset (UTC)"), html.Td(datetime.fromtimestamp(weather_data['sys']['sunset'], tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S'))])  # Row for sunset time in UTC.
                ], style={'textAlign': 'left'})  # Aligns the text inside the table to the left.
            ], style={  # Styles the table container, setting its width, border, and padding.
                'margin': 'auto', 'width': '60%', 'border': '2px solid #ddd', 'borderCollapse': 'collapse',
                'padding': '10px', 'textAlign': 'left', 'fontSize': '18px',
                'border-spacing': '0px', 'table-layout': 'fixed'
            })
        else:  # If no weather data is available...
            current_weather_output = "No data available"  # Displays a message indicating that no data is available.

        # Fetch and process 5-day forecast data
        forecast_data = get_forecast_by_coordinates(lat, lon, api_key, units=unit_system)  # Fetches the 5-day weather forecast data.
        forecast_fig = {}  # Initializes an empty dictionary for the forecast graph.
        if forecast_data:  # If forecast data is available...
            forecast_df = process_forecast_data(forecast_data)  # Processes the forecast data into a pandas DataFrame.
            forecast_fig = px.line(forecast_df, x='datetime', y='temp', title=f"5-Day Forecast for {city}")  # Creates a line graph of the forecasted temperature for the next 5 days.
            forecast_fig.update_layout(xaxis_title="Date and Time", yaxis_title="Temperature", template="plotly_dark")  # Updates the graph layout, adding axis labels and a dark theme.

        # Fetch and process historical weather data (last 5 days)
        end_time = int(datetime.now(tz=timezone.utc).timestamp())  # Gets the current timestamp in UTC.
        start_time = int((datetime.now(tz=timezone.utc) - timedelta(days=5)).timestamp())  # Calculates the timestamp for 5 days ago.
        historical_data = get_historical_weather(lat, lon, start_time, end_time, api_key, units=unit_system)  # Fetches the historical weather data for the last 5 days.
        historical_fig = {}  # Initializes an empty dictionary for the historical weather graph.
        if historical_data:  # If historical weather data is available...
            historical_df = process_historical_weather_data(historical_data)  # Processes the historical weather data into a DataFrame.
            historical_fig = px.line(historical_df, x='datetime', y='temp',
                                     title=f"Historical Weather Data for {city} - Last 5 Days")  # Creates a line graph for the last 5 days of weather data.
            historical_fig.update_layout(xaxis_title="Date and Time", yaxis_title="Temperature", template="plotly_dark")  # Updates the graph with axis labels and a dark theme.

        return current_weather_output, forecast_fig, historical_fig  # Returns the current weather, forecast, and historical weather figures.

    return "No data available", {}, {}  # Returns default values if no coordinates or data were found.


# --- Task: Running the app ---

# Run the app
if __name__ == '__main__':  # Checks if this script is being run directly (not imported).
    app.run_server(debug=True)  # Runs the Dash app in debug mode, which provides error logs and live updates.
