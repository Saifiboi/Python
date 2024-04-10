import pprint

import requests
from flight_data import FlightData


class FlightSearch:
    def __init__(self):
        self.endpoint_v2 = "https://api.tequila.kiwi.com/v2/"
        self.endpoint = "https://api.tequila.kiwi.com/"
        self.header = {
            "apikey": "m4FwWMHTnSUjBm6IoNxk1a6yFNYevjSo",
        }

    def IATA_code(self, city_name):
        paras = {
            "term": city_name,
            "locale": "en-US",
            "location_types": "city",
            "limit": 10,
            "active_only": True,
            "sort": "name"
        }
        response = requests.get(url=f"{self.endpoint}locations/query", params=paras, headers=self.header)
        if response.status_code != 200:
            raise ImportError
        return response.json()["locations"][0]["code"]

    def search_for_flights(self, city_code):
        f_data = FlightData()
        f_data.set_city(city_code)
        response = requests.get(url=f"{self.endpoint_v2}search", params=f_data.paras, headers=self.header)
        if response.status_code != 200:
            f_data.paras["max_stopovers"] = 1
            response = requests.get(url=f"{self.endpoint_v2}search", params=f_data.paras, headers=self.header)
            if response.status_code != 200:
                raise ImportError
            else:
                return response.json(), True
        else:
            return response.json(), False
