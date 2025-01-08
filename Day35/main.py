import requests

API_KEY = "API-KEY"

parameters = {
    "lat": LAT,
    "lon": LONG,
    "cnt": 4,
    "appid": API_KEY,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()
weather_list = data["list"]


def check_weather():
    for item in weather_list:
        weather = item["weather"][0]["id"]
        if weather <= 700:
            return True


if check_weather():
    print("Bring an umbrella.")
