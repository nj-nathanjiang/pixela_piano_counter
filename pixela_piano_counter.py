import requests
import datetime

USERNAME = "username"
TOKEN = "token"

pixela_endpoint = "https://pixe.la/v1/users"

headers = {
    "X-USER-TOKEN": TOKEN
}

post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

today = datetime.datetime.now()

num_minutes = input("How many minutes did you play piano for? ")

post_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": f"{num_minutes}",
}

response = requests.post(url=post_endpoint, json=post_config, headers=headers)
