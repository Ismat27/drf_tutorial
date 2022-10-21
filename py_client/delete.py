import requests

endpoint = 'http://localhost:8000/api/products/6/delete/'
endpoint2 = 'http://localhost:8000/api/products/17/'

get_response = requests.delete(endpoint2)
print(get_response.status_code)