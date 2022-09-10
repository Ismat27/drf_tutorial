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
if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        'Authorization': f'Bearer {token}'
    }
    get_response = requests.get(endpoint, headers=headers)
    print(get_response.json())
else:
    print(auth_response.status_code)
