import requests
from getpass import getpass

endpoint = 'http://localhost:8000/api/products/'
auth_endpoint = 'http://localhost:8000/api/auth/'

username = input('Username: ')
password = getpass('Password: ')
json = {
    'username': username,
    'password': password
}
auth_response = requests.post(auth_endpoint, json=json)
post_json = {
    # "title": "pearls shoes",
    "content": "awesome and expensive wrist watch",
    "price": 152.99
}
if auth_response.status_code==200:
    token = auth_response.json()['token']
    headers = {
        'Authorization': f'Bearer {token}'
    }
    get_response = requests.post(endpoint, headers=headers, json=post_json)
    print(get_response.json())
else:
    print(auth_response.status_code)