import requests
import datetime as dt
from dotenv import dotenv_values

config = {**dotenv_values(".env.secret")}

user_params = {
    "token": config["TOKEN"],
    "username": config["USERNAME"],
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{config['pixela_endpoint']}/{config['USERNAME']}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Study Graph",
    "unit": "hours",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": config["TOKEN"],
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

site = "https://pixe.la/v1/users/gcbeltrao/graphs/graph1.html"

time_now = dt.datetime.now()
today = time_now.strftime("%Y%m%d")
yesterday = dt.datetime(year=2024, month=4, day=25).strftime("%Y%m%d")

pixels_endpoint = (
    f"{config['pixela_endpoint']}/{config['USERNAME']}/graphs/{config['GRAPH_ID']}"
)

graph_pixels = {
    "date": today,
    "quantity": input("How many hours did you study today?"),
}

response = requests.post(url=pixels_endpoint, json=graph_pixels, headers=headers)
print(response.text)

update_endpoint = f"{config['pixela_endpoint']}/{config['USERNAME']}/graphs/{config['GRAPH_ID']}/{yesterday}"

update_pixels = {
    "quantity": "2.5",
}

# response = requests.put(url=update_endpoint, json=update_pixels, headers=headers)
# print(response.text)

delete_endpoint = f"{config['pixela_endpoint']}/{config['USERNAME']}/graphs/{config['GRAPH_ID']}/{today}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
