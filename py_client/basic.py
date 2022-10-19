import requests

endpoint = 'http://localhost:8000/api/'

post_json = {
    "title": "gucci trouser"
}
headers = {
    "Authorization": "BEARER ff2a2296596403f3072e7a64cf2c3368951747cf"
}
get_response = requests.post(endpoint, params={'search_term': 'html'}, headers=headers, json=post_json)
print(get_response.json())