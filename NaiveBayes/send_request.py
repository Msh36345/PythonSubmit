import requests
from pprint import pprint
# API_URL = 'http://127.0.0.1:8080/'
API_URL = 'http://127.0.0.1:8080/moshe'


response = requests.get(API_URL)
print(response)
print(response.status_code)
pprint(response.json())