import requests
import json
import ast

class RequestData:
    def __init__(self):
        self.url = "http://naivebayes-host:8070"
        self.response = requests.get(self.url)
        self.dic = json.loads(self.response.text)
        self.my_dict = ast.literal_eval(self.dic)
