import requests
endpoint = "http://localhost:8000/api/products/0973645080987059093458709387"

get_response = requests.get(endpoint)
print(get_response.json())