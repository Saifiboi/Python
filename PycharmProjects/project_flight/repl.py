import json

import requests

print("Welcome to Saifi's Flight Club.")
print("We find the best flight deals and email you.")
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
email = input("What is your email? ")
counter = 1
check = False
while email != input("Please confirm your email.") and counter <= 3:
    if counter == 3:
        check = True
        break
    else:
        print("Singup Attempt Fail! Retry..")
        first_name = input("What is your first name? ")
        last_name = input("What is your last name? ")
        email = input("What is your email? ")
        counter += 1
if not check:
    print("You are in the club.")
    head = {
            # "Authorization": "Bearer I am Saifi",
            "Content-Type": "application/json"
            }
    data = {
        "user": {
            "fName": first_name,
            "lName": last_name,
            "email": email
        }
    }
    print(data)
    response = requests.post(url="https://api.sheety.co/ab014967b6b4b6de88b95d46166dc6a4/flights/users",
                             data=json.dumps(data), headers=head)
    print(response.status_code)
else:
    print("Breach ! Program aborted..")
