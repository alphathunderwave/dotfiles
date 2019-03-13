#!/usr/bin/env python3
import pyowm

owm = pyowm.OWM('8a998eba2ea925f64e8aa4dd8ae7f1eb')  # You MUST provide a valid API key

# Have a pro subscription? Then use:
# owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

# Search for current weather in London (Great Britain)
observation = owm.weather_at_place('Buffalo')
w = observation.get_weather()
print( str(int(w.get_temperature('fahrenheit')['temp'])) + "°F" )
