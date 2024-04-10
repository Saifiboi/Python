# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
from data_manager import DataManager
from flight_search import FlightSearch

from notification_manager import notify_me

sheet_obj = DataManager()
flight_searcher = FlightSearch()
try:
    sheet_data = sheet_obj.sheet_data()["prices"]
except ImportError:
    print("Not got prices data go check data manager class in detail..")
    exit(-1)
dta_dev = {"price": "",
           }
if any(dic["iataCode"] == "" for dic in sheet_data):
    index = 2
    for data in sheet_data:
        try:
            data["iataCode"] = flight_searcher.IATA_code(data["city"])
        except ImportError:
            print("Not got IATA code for cities.Go check FlightSearch class in detail..")
            exit(-2)
        dta_dev["price"] = data
        try:
            sheet_obj.put_on_sheet(dta_dev, index)
        except ImportError:
            print("Unable to put data on sheets.Go check data manager class in detail..")
            exit(-3)
        index += 1
for data in sheet_data:
    try:
        flight_results, stop_over = flight_searcher.search_for_flights(data["iataCode"])
    except ImportError:
        continue
    if len(flight_results["data"]) != 0:
        for i in flight_results["data"]:
            if (i["availability"]["seats"] is not None) and i["availability"]["seats"] > 0:
                if i["price"] < data["lowestPrice"]:
                    notify_me(i, sheet_obj.get_userdata(), stop_over)
