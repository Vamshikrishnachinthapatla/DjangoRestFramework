import requests

endpoint = "http://localhost:8000/api/products/5/update/" 

data = {
    "title": "OLA world",
    "content":"THIS IS MUCH MORE AWESOME",
    "price": 1.00
}

get_response = requests.put(endpoint, json=data) 
print(get_response.json())