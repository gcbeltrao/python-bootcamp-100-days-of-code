import time
import requests
from datetime import datetime
import smtplib

MY_EMAIL = "email@gmail.com"
PASSWORD = "" #PUT YOUR PASSWORD HERE

MY_LAT = 0 #PUT YOUR LATITUDE HERE
MY_LONG = 0 #PUT YOUR LONGITUDE HERE


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    range_min_lat = MY_LAT - 5
    range_max_lat = MY_LAT + 5
    range_min_lng = MY_LONG - 5
    range_max_lng = MY_LONG + 5

    if range_min_lat <= iss_latitude <= range_max_lat and range_min_lng <= iss_longitude <= range_max_lng:
        return True


# Your position is within +5 or -5 degrees of the ISS position.

def its_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hour = time_now.hour

    if hour >= sunset or hour <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and its_dark():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:Satelite a vista!\n\nTexto: Satélite está próximo da sua localização e está disponível "
                    f"para ser observado.")
