import requests
endpoint = "http://localhost:8000/api/products/"


data = {
    "title":"THIS FIELD IS DONE",
    "price":32.99
}

get_response = requests.post(endpoint, json=data)
print(get_response.status_code) # See if it's 404, 500, etc.
if get_response.status_code != 200:
    print(get_response.text) # This will show the HTML error from Django
else:
    print(get_response.json())