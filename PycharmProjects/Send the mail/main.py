import datetime as dt
import random
import smtplib

#


with open("quotes.txt", mode='r') as file:
    list_q = file.readlines()

date_obj = dt.datetime.now()
quote = ""
if date_obj.weekday() == 6:
    quote = random.choice(list_q)
    my_email = "belachao774@gmail.com"
    my_password = "Niazi774_"
    to_another_mail = "innominate.0b1@gmail.com"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(to_addrs=to_another_mail,
                            from_addr=my_email,
                            msg=quote)
