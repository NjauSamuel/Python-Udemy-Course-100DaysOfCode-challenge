# # The following is how the responses' module works.
#
# """
# 1XX: Hold On
# 2XX: Here you go, the request is successful
# 3XX: Go Away
# 4XX: You screwed up
# 5XX: I screwed up/ Or they screwed up.
#
# """
#
# # The simple requests code is as follows:
# import requests
#
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# print(data)


import requests
import datetime

MY_LAT = -0.303099
MY_LONG = 36.080025

parameters = {
    "latt": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise.split("T")[1].split(":")[0])
print(sunset.split("T")[1].split(":")[0])

time_now = datetime.datetime.now()

print(time_now.hour)
