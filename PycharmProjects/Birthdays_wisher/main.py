##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
import datetime as db
import smtplib
import pandas
import random
MY_EMAIL = "belachao774@gmail.com"
MY_PASSWORD = "hajkvzgsyhjdgeek"
today = db.datetime.now()
my_panda = pandas.read_csv("birthdays.csv")
dict_b = my_panda.to_dict(orient='index')
letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
for di in dict_b.values():
    if today.day == di["day"] and today.month == di["month"]:
        lett = random.choice(letters)
        with open(f"./letter_templates/{lett}", mode='r') as file:
            data = file.read()
        new_data = data.replace("[NAME]", di["name"])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg=f"Subject:Happy Birthday\n\n{new_data}")



# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv


# 4. Send the letter generated in step 3 to that person's email address.
