# import requests
#
# key = "4fcc5c746c83d182ca016014804d1db3"
#
# para = {
#     "lat": 33.684422,
#     "lon": 73.047882,
#     "appid": key,
#     "exclude":"current,minutely,daily"
# }
# response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=para)
# print(response.json())
from twilio.rest import Client
acc_sid = "AC9842f3a9d9d780edf7a92b75bde0c4f0"
auth_tok = "90f896cc2d026e464daec9ecc115483b"
client = Client(acc_sid, auth_tok)
message = client.messages.create(body="Maa Uva Saalia!",
from_="+14323093892", to="+923135362340")
print(message.status)
