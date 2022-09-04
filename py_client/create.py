import requests

endpoint = 'http://localhost:8000/api/products/'

post_json = {
    "title": "diamond",
    # "content": "awesome and expensive wrist watch",
    "price": 152.99
}
get_response = requests.post(endpoint, params={'search_term': 'html'}, json=post_json)
print(get_response.json())