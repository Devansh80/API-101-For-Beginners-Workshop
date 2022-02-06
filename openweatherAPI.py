from urllib import response
import requests
import json

API_KEY = "a1d25fe4f55e94d12fe2151c5b3c19b4"
city_name = input("Enter city name ")

URL = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}"

response = requests.get(URL)
json_data = json.loads(response.text)

weather = json_data["weather"][0]["description"]
temprature = json_data["main"]["temp"]
temp_in_celsius = temprature - 273.15
humidity = json_data["main"]["humidity"]
wind_speed = json_data["wind"]["speed"]

print(f"Weather: {weather}")
print(f"Temprature: {int(temp_in_celsius)}")
print(f"Humidity: {humidity}")
print(f"Wind Speed: {wind_speed}")
