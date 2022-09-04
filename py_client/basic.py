import requests

endpoint = 'http://localhost:8000/api/'

post_json = {
    "title": "gucci trouser"
}
get_response = requests.post(endpoint, params={'search_term': 'html'}, json=post_json)
print(get_response.json())