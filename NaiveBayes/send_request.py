import requests
from pprint import pprint
# API_URL = 'http://127.0.0.1:8080/'
# API_URL = 'http://127.0.0.1:8080/moshe'
API_URL = 'http://127.0.0.1:8080/dict?age=senior&income=high&student=no&credit_rating=fair'


response = requests.get(API_URL)
print(response)
print(response.status_code)
pprint(response.json())