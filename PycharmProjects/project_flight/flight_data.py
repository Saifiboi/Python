import datetime as dt
from dateutil.relativedelta import relativedelta


class FlightData:
    def __init__(self):
        date_today = dt.datetime.now().strftime("%d/%m/%Y")
        date_6 = dt.date.today() + relativedelta(months=+6)
        self.paras = {
            "fly_from": "ISB",
            "fly_to": "",
            "date_from": date_today,
            "date_to": date_6.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "ret_from_diff_city": False,
            "ret_to_diff_city": False,
            "selected_cabins": "M",
            "curr": "GBP",
            # "price_from": 0,
            # "price_to": 0,
            "vehicle_type": "aircraft",
            "max_stopovers": 0

        }

    def set_city(self, city_code):
        self.paras["fly_to"] = city_code


