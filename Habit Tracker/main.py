import  requests
from datetime import datetime

USERNAME = "kunjesh0402"
TOKEN = "abcd1234"
GRAPH_ID = "graph01"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token" : "abcd1234",
    "username" : "kunjesh0402",
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}
#
# response = requests.post(url=pixela_endpoint, json= user_params)
# print(response)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id" : "graph01",
    "name" : "Cycling Graph",
    "unit" : "Km",
    "type" : "float",
    "color" : "sora",
}
headers = {
    "X-USER-TOKEN" : TOKEN
}
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime.now()
print(today)

pixel_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
pixel_params = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : input("How many Kms you cycled today ? : "),
}
#
# response = requests.post(url=pixel_creation_endpoint, json=pixel_params, headers=headers)
# print(response.text)

update_endpoint = f"{pixel_creation_endpoint}/{pixel_params['date']}"
update_info = {
    "quantity" : "17.5"
}

# response = requests.put(url=update_endpoint, json=update_info, headers=headers)
# print(response)

delete_endpoint = f"{update_endpoint}"
#
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
