import requests

endpoint = 'http://localhost:8000/api/products/'

data = {
    "title": "THis field is done"
}
get_response = requests.get(endpoint)

print(get_response.json())