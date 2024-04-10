import json

import requests
from pprint import pprint


class DataManager:
    def __init__(self):
        self.url = "https://api.sheety.co/9af17019b87e3c51549e6cb4512d796f/flights/"
        self.head = {
            "Authorization": "Basic U2FpZmk6Tmlhemk5OV8=",
            "Content-Type": "application/json",
        }

    def sheet_data(self):
        response = requests.get(url=f"{self.url}prices",
                                headers=self.head)
        if response.status_code != 200:
            raise ImportError
        return response.json()

    def get_userdata(self):
        response = requests.get(url=f"{self.url}users", headers=self.head)
        return response.json()

    def put_on_sheet(self, sheet_data, index):
        response = requests.put(
            url=f"{self.url}prices/{index}",
            headers=self.head, data=json.dumps(sheet_data))
