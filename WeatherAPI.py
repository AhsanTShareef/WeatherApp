from fastapi import FastAPI, HTTPException
import pandas as pd
import requests

# Import US Data
see = pd.read_csv(r"us_cities.csv")

app = FastAPI()
API_key = 'f74697402610092ac90b3ba16bea0528'  # API key pulled from openweathermap.org. Hard code for API key in URL


def lat_long(state: str, city: str, county: str):
    # If the city, state name, and county match then it will return the specific rows data you are asking for.
    # Access the specific row using .loc[] and iloc[] then stored the output of latitude and longitude values.
    lat = see.loc[(see['CITY'] == city) & (see['STATE_NAME'] == state) & (see['COUNTY'] == county), 'LATITUDE'].iloc[0]
    lon = see.loc[(see['CITY'] == city) & (see['STATE_NAME'] == state) & (see['COUNTY'] == county), 'LONGITUDE'].iloc[0]


    # .get function is used to access data for a server.
    # Make a request to OpenWeatherMap API
    URL = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}'
    try:
        response = requests.get(URL)
        response.raise_for_status() #Raise an exception for HTTP errors, such as connection or error response from server
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=503, detail = 'Server unavailable')


@app.get("/temperature")  # Temperature page for our domain
def temp(state: str, city: str, county: str):
    try:
        results = lat_long(state, city, county)
        temperature = results['main']['temp']
        temp = round(((temperature - 273.15) * (9 / 5) + 32), 2)
        return f'Temp: {temp}°F '
    except IndexError:
        raise HTTPException(status_code=404, detail = 'City, State, or County not found.')
    except KeyError:
        raise HTTPException(status_code=500, detail='Weather data error')


@app.get("/humidity")  # Humidity page for our domain
def humidity(state: str, city: str, county: str):
    try:
        results = lat_long(state, city, county)
        humidity = results['main']['humidity']
        return f'Humidity: {humidity}% '
    except IndexError:
        raise HTTPException(status_code=404, detail = 'City, State, or County not found.')
    except KeyError:
        raise HTTPException(status_code=500, detail='Weather data error')


@app.get("/weather")  # Weather description page for our domain
def weather(state: str, city: str, county: str):
    try:
        results = lat_long(state, city, county)
        weather_description = results['weather'][0]['description']
        return f' Weather Description: {weather_description}'
    except IndexError:
        raise HTTPException(status_code=404, detail = 'City, State, or County not found.')
    except KeyError:
        raise HTTPException(status_code=500, detail='Weather data error')



@app.get("/windspeed")  # Weather description page for our domain
def windspeed(state: str, city: str, county: str):
    try:
        results = lat_long(state, city, county)
        wind_speed = results['wind']['speed']
        return f'Windspeed: {wind_speed} mph'
    except IndexError:
        raise HTTPException(status_code=404, detail = 'City, State, or County not found.')
    except KeyError:
        raise HTTPException(status_code=500, detail='Weather data error')


@app.post("/coordinates")  # Returns weather data based on coordinates sent by user.
def coordinates(latitude: float, longitude: float):
    # .get function is used to access data for a server.
    URL = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_key}'
    response = requests.get(URL)

    # results turns the information pulled from the server into json format.
    try:
        results = response.json()
        city_name = results['name']

        temperature = results['main']['temp']
        temp = round(((temperature - 273.15) * (9 / 5) + 32), 2)

        weather_description = results['weather'][0]['description']
        weather_desc = (weather_description.capitalize())

        humidity = results['main']['humidity']

        wind_speed = results['wind']['speed']
        return (f'City Name: {city_name}',
                f'Temperature(fahrenheit): {temp}°F',
                f'Weather Description: {weather_desc}',
                f'Humidity: {humidity}%',
                f'Wind Speed: {wind_speed} mph')
    except IndexError:
        raise HTTPException(status_code=404, detail = 'Latitude or Longitude not found.')
    except KeyError:
        raise HTTPException(status_code=500, detail='Weather data error')
