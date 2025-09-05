import requests

API_KEY = "a493410b3a2a9434eea0bef32533cb53"  # Replace with your OpenWeatherMap API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")
params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(BASE_URL, params=params)
if response.status_code == 200:
    data = response.json()
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    print(f"Weather in {city}: {desc.capitalize()}, {temp}°C")
else:
    print("City not found or API error.")