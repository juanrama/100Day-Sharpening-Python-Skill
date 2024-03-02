import requests
import json
import datetime as dt
import smtplib
import time

MY_LAT = -48.8244
MY_LONG = 146.1929
EMAIL = "76.zulfikar@gmail.com"
PASS = "jfmnscbvjtzpzzja"


def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    data = response.json()
    
    longitude = float(data['iss_position']['longitude'])
    latitude = float(data['iss_position']['latitude'])
    
    if abs(MY_LAT - latitude) <= 5 and abs(MY_LONG - longitude) <= 5:
        return True

def is_night():
    time_now = dt.datetime.now()

    parameter = {
            'lat' : MY_LAT,
            'lng' : MY_LONG,
            'formatted' : 0,
            'tzid' : 'Asia/Jakarta'
        }
    response_sun = requests.get(url = 'https://api.sunrise-sunset.org/json', params=parameter)
    sunrise = response_sun.json()['results']['sunrise'].split('T')[1].split(':')[0]
    sunset = response_sun.json()['results']['sunset'].split('T')[1].split(':')[0]
    if time_now.hour < int(sunrise) or time_now.hour > int(sunset):
        return True


while True:
    time.sleep(60)
    if iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connect:
            connect.starttls()
            connect.login(user=EMAIL, password=PASS)
            connect.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg="Subject:ISS Coming\n\nLook at above you Rama!! ISS is coming")
            