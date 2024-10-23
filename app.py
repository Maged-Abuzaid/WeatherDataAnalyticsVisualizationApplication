import os
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
from datetime import datetime, timezone, timedelta

from weather.current_weather import get_weather_by_coordinates, process_weather_data, get_city_coordinates
from weather.forecast import get_forecast_by_coordinates, process_forecast_data
from weather.historical_weather import get_historical_weather, process_historical_weather_data

# Get the API key from the system environment variable
api_key = os.getenv("WEATHER_API_KEY")

if not api_key:
    raise ValueError("API key not found in environment variables. Make sure WEATHER_API_KEY is set.")

# Initialize Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    html.H1("Interactive Weather Dashboard", style={'textAlign': 'center', 'padding-bottom': '20px'}),

    # Create a flexible layout for the city input and submit button (above temperature selection)
    html.Div([
        html.Label("Enter city name for weather analysis (e.g., London):", style={'margin-right': '10px'}),
        dcc.Input(id='city-input', value='London', type='text', style={'width': '300px', 'margin-right': '20px'}),
        html.Button('Submit', id='submit-button', n_clicks=0),
    ], style={'textAlign': 'center', 'padding': '20px 0'}),

    # Centered block for temperature unit selection
    html.Div([
        html.Label("Select temperature unit:", style={'margin-right': '10px'}),
        dcc.Dropdown(
            id='unit-dropdown',
            options=[
                {'label': 'Celsius (°C)', 'value': 'metric'},
                {'label': 'Fahrenheit (°F)', 'value': 'imperial'}
            ],
            value='metric',
            style={'width': '200px', 'margin': '0 auto'}
        ),
    ], style={'textAlign': 'center', 'padding': '10px 0'}),

    # Current weather output in table format
    html.Div(id='current-weather-output', style={'padding': '20px', 'text-align': 'center', 'font-size': '18px'}),

    # Graphs for forecast and historical weather
    dcc.Graph(id='forecast-graph'),
    dcc.Graph(id='historical-weather-graph')
])


# Callback to update current weather, forecast graph, and historical weather graph
@app.callback(
    [Output('current-weather-output', 'children'),
     Output('forecast-graph', 'figure'),
     Output('historical-weather-graph', 'figure')],
    [Input('submit-button', 'n_clicks')],
    [dash.dependencies.State('city-input', 'value'),
     dash.dependencies.State('unit-dropdown', 'value')]
)
def update_weather_dashboard(n_clicks, city, unit_system):
    coordinates = get_city_coordinates(city, api_key)
    if coordinates:
        lat, lon = coordinates['lat'], coordinates['lon']

        # Fetch and display current weather data
        weather_data = get_weather_by_coordinates(lat, lon, api_key, units=unit_system)
        if weather_data:
            # Structure the current weather data into a table with better styling
            current_weather_output = html.Table([
                html.Thead(html.Tr([html.Th("Weather Parameter"), html.Th("Value")]),
                           style={'backgroundColor': '#4CAF50', 'color': 'white'}),
                html.Tbody([
                    html.Tr([html.Td("Temperature"), html.Td(f"{weather_data['main']['temp']}°")]),
                    html.Tr([html.Td("Feels Like"), html.Td(f"{weather_data['main']['feels_like']}°")]),
                    html.Tr([html.Td("Min Temperature"), html.Td(f"{weather_data['main']['temp_min']}°")]),
                    html.Tr([html.Td("Max Temperature"), html.Td(f"{weather_data['main']['temp_max']}°")]),
                    html.Tr([html.Td("Humidity"), html.Td(f"{weather_data['main']['humidity']}%")]),
                    html.Tr([html.Td("Pressure"), html.Td(f"{weather_data['main']['pressure']} hPa")]),
                    html.Tr([html.Td("Wind Speed"), html.Td(f"{weather_data['wind']['speed']} m/s")]),
                    html.Tr([html.Td("Cloudiness"), html.Td(f"{weather_data.get('clouds', {}).get('all', 'N/A')}%")]),
                    html.Tr([html.Td("Sunrise (UTC)"), html.Td(
                        datetime.fromtimestamp(weather_data['sys']['sunrise'], tz=timezone.utc).strftime(
                            '%Y-%m-%d %H:%M:%S'))]),
                    html.Tr([html.Td("Sunset (UTC)"), html.Td(
                        datetime.fromtimestamp(weather_data['sys']['sunset'], tz=timezone.utc).strftime(
                            '%Y-%m-%d %H:%M:%S'))])
                ], style={'textAlign': 'left'})
            ], style={
                'margin': 'auto', 'width': '60%', 'border': '2px solid #ddd', 'borderCollapse': 'collapse',
                'padding': '10px', 'textAlign': 'left', 'fontSize': '18px',
                'border-spacing': '0px', 'table-layout': 'fixed'
            })
        else:
            current_weather_output = "No data available"

        # Fetch and process 5-day forecast data
        forecast_data = get_forecast_by_coordinates(lat, lon, api_key, units=unit_system)
        forecast_fig = {}
        if forecast_data:
            forecast_df = process_forecast_data(forecast_data)
            forecast_fig = px.line(forecast_df, x='datetime', y='temp', title=f"5-Day Forecast for {city}")
            forecast_fig.update_layout(xaxis_title="Date and Time", yaxis_title="Temperature", template="plotly_dark")

        # Fetch and process historical weather data (last 5 days)
        end_time = int(datetime.now(tz=timezone.utc).timestamp())
        start_time = int((datetime.now(tz=timezone.utc) - timedelta(days=5)).timestamp())
        historical_data = get_historical_weather(lat, lon, start_time, end_time, api_key, units=unit_system)
        historical_fig = {}
        if historical_data:
            historical_df = process_historical_weather_data(historical_data)
            historical_fig = px.line(historical_df, x='datetime', y='temp',
                                     title=f"Historical Weather Data for {city} - Last 5 Days")
            historical_fig.update_layout(xaxis_title="Date and Time", yaxis_title="Temperature", template="plotly_dark")

        return current_weather_output, forecast_fig, historical_fig

    return "No data available", {}, {}


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
