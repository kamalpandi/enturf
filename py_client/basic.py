import requests

endpoint = "http://127.0.0.1:8000/update_admin/2"


get_responce = requests.get(endpoint)
#print(get_responce.text)

print(get_responce.json())
#print(get_responce.status_code)