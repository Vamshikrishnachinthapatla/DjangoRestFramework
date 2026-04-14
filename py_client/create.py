import requests


headers = {'Authorization': 'Bearer 22f110753a3fa86499d7fcc8214414d5423d5a51'}

endpoint = "http://localhost:8000/api/products/"



data = {
    "title":"OLA IAM MESSI",
    "content":"This is from the fan VAMSHI",
    "price":32.99,
}

get_response = requests.post(endpoint, json=data, headers=headers)

print(get_response.json())