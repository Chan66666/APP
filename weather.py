import requests
import json
api_key = "YOUR_API_KEY"
base_url = "YOUR_API_URL"
option = input("Enter 'current' to get weather for your current location or 'city' to enter a specific city: ")

if option == 'current':
    # Get user's current location using a geolocation API
    # code to get current location goes here
    latitude = ...
    longitude = ...
else:
    city = input("Enter a city name: ")
if option == 'current':
    url = f"{base_url}?lat={latitude}&lon={longitude}&appid={api_key}"
else:
    url = f"{base_url}?q={city}&appid={api_key}"

response = requests.get(url)
data = response.json()
if data["cod"] == 200:
    main_weather = data["weather"][0]["main"]
    description = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]

    print(f"Weather: {main_weather} - {description}")
    print(f"Temperature: {temperature} K")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
else:
    print("Error occurred while retrieving weather data.")
