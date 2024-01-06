import datetime
import random
import smtplib

import pandas

MY_EMAIL = "njaus604@gmail.com"
MY_PASSWORD = "xdrn zkob ohjs rxcc"

# 2. Check if today matches a birthday in the birthdays.csv
today = datetime.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
# 3. Use dictionary comprehension to create a dictionary from birthday.csv that is formatted like this:

# Dictionary comprehension template for pandas DataFrame looks like this:
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}


# 4. Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
if today_tuple in birthdays_dict:
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        birthday_person = birthdays_dict[today_tuple]
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_person["email"], msg=f"Subject:Happy Birthday!\n\n{contents}")


