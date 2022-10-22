import requests

endpoint = 'http://localhost:8000/api/products/15/test/'

post_json = {
    "title": "pair of gucci trousers",
    "content": "latest pair gucci trousers",
    "price": 300
}
get_response = requests.put(endpoint, json=post_json)
print(get_response.json())