import requests
import config
from pprint import pprint
from functions import tempAndFeelsLike, highLowTemp, checkWeather

BASE_url = "http://api.openweathermap.org/data/2.5/weather?"
FINAL_url = BASE_url + "appid=" + config.api_key + "&q=Florida"

weather_data = requests.get(FINAL_url).json()

# pprint(weather_data)
badWeather = weather_data['weather'][0]['description']

currentTemp = weather_data['main']['temp']
feelsLikeTemp = weather_data['main']['feels_like']

highTemp = weather_data['main']['temp_max']
lowTemp = weather_data['main']['temp_min']
humidity = weather_data['main']['humidity']

print("\nCurrent Weather Data Of Chicago:\n")
tempAndFeelsLike(currentTemp, feelsLikeTemp)
highLowTemp(highTemp, lowTemp, humidity)
checkWeather(badWeather)
checkWeather("rain")
# thunderstorm, rain
