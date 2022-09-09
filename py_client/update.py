import requests

endpoint = 'http://localhost:8000/api/products/4/update/'

post_json = {
    "title": "gucci trousers",
    "content": "latest gucci trousers",
    "price": 300
}
get_response = requests.put(endpoint, json=post_json)
print(get_response.json())