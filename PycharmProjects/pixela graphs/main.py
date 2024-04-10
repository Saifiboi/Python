import requests
import datetime

end_point = " https://pixe.la/v1/users/saifi/graphs/codegraph/"
params = {
    "token": "&dx9z2A1F6(+Tkc)Zl",
    "username": "saifi",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
user_tok = {
    "X-USER-TOKEN": "&dx9z2A1F6(+Tkc)Zl",
}
new_paras = {
    "quantity": "10",
}
# response = requests.post(url=end_point, json=params)
# print(response.text)
date = datetime.datetime.now().strftime("%Y%m%d")
print(f"{end_point}{date}")
response = requests.delete(url=f"{end_point}{date}", headers=user_tok)
print(response.text)
