import requests
import datetime as dt

MY_LAT = 0 #PUT YOUR LATITUDE HERE
MY_LONG = 0 #PUT YOUR LONGITUDE HERE

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

time_now = dt.datetime.now()

print(sunrise)
print(sunset)
