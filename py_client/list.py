import requests

endpoint = 'http://localhost:8000/api/products/'

get_response = requests.get(endpoint, params={'search_term': 'html'})
print(get_response.json())