import requests

endpoint = 'http://localhost:8000/api/products/1/'

post_json = {
    "title": "gucci trouser"
}
get_response = requests.get(endpoint, params={'search_term': 'html'}, json=post_json)
print(get_response.json())