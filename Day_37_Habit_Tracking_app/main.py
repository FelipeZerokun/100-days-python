import requests
import os
from datetime import datetime

# Following the steps in https://pixe.la/
USERNAME = os.environ['PIXELA_USERNAME']
TOKEN = os.environ['PIXELA_TOKEN']
GRAPH_ID = 'graph1'


# First step. Create user name
pixela_endpoint = 'https://pixe.la/v1/users'      # This one is to Create a user
create_user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url= pixela_endpoint, json=create_user_params)
# print(response.text)
# I comment it out because my user is already created

# Second step. Create a Graph definition

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
graph_config = {
    'id': GRAPH_ID,
    'name': 'running_graph',
    'unit': 'Km',
    'type': 'float',
    'color': 'momiji'
}

headers = {
    'X-USER-TOKEN': TOKEN
    }

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
# Commented out after created the graph

# Third step. Send data for the graph!
pixel_creation_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'

today = datetime.now()
today = today.strftime("%Y%m%d")
# print(today)
pixel_config = {
    'date': today,
    'quantity': input("How many KM did you run today?: "),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_config, headers=headers)
print(response.text)


# ##### Update a graph configuration
# update_graph_url = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'
# update_config = {
#     'name': "New Name",
#     'unit': "calory",
# }
#
# response = requests.put(url=update_graph_url, json= update_config, headers=headers)
#
# ##### Update pixel data
# update_pixel_url = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}'
# update_config = {
#     'quantity': "12"
# }
#
# response = requests.put(url=update_graph_url, json= update_config, headers=headers)
#
# ###### Delete a pixel in a graph
# delete_graph_url = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}'
# response = requests.delete(url=delete_graph_url, headers=headers)