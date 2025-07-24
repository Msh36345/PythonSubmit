import requests
import json
import ast

class RequestData:
    def __init__(self):
        self.url = 'http://127.0.0.1:8070'
        self.response = requests.get(self.url)
        self.dic = json.loads(self.response.text)
        self.my_dict = ast.literal_eval(self.dic)
