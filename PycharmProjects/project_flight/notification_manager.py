# from twilio.rest import Client    #library for message sending.
from smtplib import SMTP

msg = ""


def notify_me(flight, user_data, stop_over):
    global msg
    user_list = user_data["users"]
    for user in user_list:
        user_name = f"{user['fName']} {user['lName']}"
        try:
            email = user["email"]
        except KeyError:
            continue
        if not stop_over:
            msg = f"""
                   Dear {user_name},
                   You have a cheap flight oppurtunity!
                   Price : £{flight['price']}
                   Departure City Name: {flight['cityFrom']}
                   Departure Airport IATA Code: {flight['flyFrom']}
                   Arrival City Name: {flight['cityTo']}
                   Arrival Airport IATA Code: {flight['flyTo']}
                   Outbound Date: {flight['local_arrival'].split('T')[0]}
                   Nights of Stay: {flight['nightsInDest']}
                   Inbound Date: {flight['route'][1]['local_arrival'].split('T')[0]}
             """

        else:
            route = flight["route"]["route"]
            num_stopovers = len(route) - 2  # Subtracting the origin and destination
            if num_stopovers > 0:
                stopover_city = route[1]  # The stopover city is at index 1
                msg = f"""
                    Dear {user_name},
                    You have a cheap flight oppurtunity!
                    Price : £{flight['price']}
                    Departure City Name: {flight['cityFrom']}
                    Departure Airport IATA Code: {flight['flyFrom']}
                    Arrival City Name: {flight['cityTo']}
                    Arrival Airport IATA Code: {flight['flyTo']}
                    Outbound Date: {flight['local_arrival'].split('T')[0]}
                    Nights of Stay: {flight['nightsInDest']}
                    Inbound Date: {flight['route'][1]['local_arrival'].split('T')[0]}
                    The flight has {num_stopovers} Stopover in {stopover_city} 
                """
        with SMTP("smtp.gmail.com") as connection:  # code for mail writing
            print("came to write email")
            try:
                connection.starttls()
                connection.login(user="belachao774@gmail.com", password="tpwftehbjngnvesp")
                connection.sendmail(from_addr="belachao774@gmail.com", to_addrs=email,
                                    msg=f"Subject:Cheap Flights in your way!\n\n{msg}")
            except OSError:
                print("Os is doing glitches")
                exit(-4)

        # sid = "AC9842f3a9d9d780edf7a92b75bde0c4f0"        //code for sms writing.
        # auth_tok = "90f896cc2d026e464daec9ecc115483b"
        # client = Client(sid, auth_tok)
        # mesg = client.messages.create(body=msg, from_="+14323093892", to="+923135362340")
        # print(mesg.status)
