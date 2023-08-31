# WeatherApp
This respository contains a FastAPI-based API that provides weather information based on location cooridinates or city/state/county information. It leverages
the OpenWeatherMap API for weather data and a CSV file containig US cities for location details. 

## Prerequisites

- Python 3.x
- FastAPI
- Pandas 
- Requests

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repository.git

Install the required dependencies:
   pip install fastapi pandas request

Usage

1. Launch the FastAPI application:
  uvicorn main:app --reload
2. Access the API endpoints in your browser or using a tool like curl or httpie.


API Endpoints

Get Temperature
  Get the temperature in Fahrenheit for a given location.

  Endpoint: /temperature

  Parameters:

  state (string): State name
  city (string): City name
  county (string): County name


Get Humidity
  Get the humidity percentage for a given location.

  Endpoint: /humidity

  Parameters:

  state (string): State name
  city (string): City name
  county (string): County name


Get Weather Description
  Get the weather description for a given location.
  
  Endpoint: /weather
  
  Parameters:
  
  state (string): State name
  city (string): City name
  county (string): County name

  
Get Wind Speed
  Get the wind speed in mph for a given location.
  
  Endpoint: /windspeed
  
  Parameters:
  
  state (string): State name
  city (string): City name
  county (string): County name

  
Get Weather by Coordinates
  Get weather information using latitude and longitude.
  
  Endpoint: /coordinates
  
  Parameters:
  
  latitude (float): Latitude coordinate
  longitude (float): Longitude coordinate

Note

  This project uses FastAPI to create a web API.
  Weather data is fetched from the OpenWeatherMap API.
  Location details are sourced from a CSV file containing US cities data.

License

  This project is licensed under the MIT License.





