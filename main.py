#http get, post(add data), put(change existing data), delete requests

import requests
from datetime import datetime

MY_TOKEN = "mrunalllll"
MY_USERNAME = "mrunalb"
GRAPH_ID = "graph1"
pixela_endpt = "https://pixe.la/v1/users"


user_params = {
    "token": MY_TOKEN,
    "username": MY_USERNAME ,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}

# response = requests.post(url=pixela_endpt, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpt}/{MY_USERNAME}/graphs"
#https://pixe.la/v1/users/mrunalb/graphs
graph_config = {
    "id" : "graph1",
     "name" : "Study Tracker",
     "unit" : "mins",
    "type" : "float",
    "color" : "ajisai"
}
headers = {
    "X-USER-TOKEN": MY_TOKEN
}
# response = requests.post(url=graph_endpoint,json=graph_config, headers=headers )
# print(response.text)

post_endpt = f"{graph_endpoint}/{GRAPH_ID}"
today = datetime.now()
print(today.strftime("%Y%m%d"))

post_config = {
    "date" : today.strftime("%Y%m%d"),  #formats string acc to our need
    "quantity" : input("How many minutes did you study today?")
}

response = requests.post(url=post_endpt, json=post_config, headers=headers)
print(response.text)

# update_pixel_endpt = f"{post_endpt}/today.strftime('%Y%m%d')"
#
# new_pixel_data = {
#     "quantity" : "23"
# }
#
# response = requests.put(url=update_pixel_endpt, json=new_pixel_data, headers=headers)
# print(response.text)




