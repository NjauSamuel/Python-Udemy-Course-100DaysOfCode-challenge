# import smtplib
# import datetime as dt
#
# my_email = "njaus604@gmail.com"
# password = "xdrn zkob ohjs rxcc"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="snjau96@yahoo.com",
#                         msg="Subject:Hello\n\nThis is my first ever Python sent email and I'm very happy from it.")
#
# Monday Motivation Project
import smtplib
import datetime as dt
import random

MY_EMAIL = "njaus604@gmail.com"
MY_PASSWORD = "xdrn zkob ohjs rxcc"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 6:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )
