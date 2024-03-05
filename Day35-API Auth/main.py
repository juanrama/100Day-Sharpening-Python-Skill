import os
import requests
from twilio.rest import Client

account_sid = os.environ.get('AUTH_APPID')
auth_token = os.environ.get('AUTH_TOKEN')
client = Client(account_sid, auth_token)

PARAM = {
    'appid' : '9067321ced3dd1631cff0d33602915cf',
    'lat' : -6.1753942,
    'lon' : 106.827183,
    'cnt' : 4
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=PARAM)
data = response.json()

is_rain = False
for i in range(len(data['list'])):
    if data['list'][i]['weather'][0]['id'] < 700:
        is_rain = True

if is_rain:
    message = client.messages.create(from_='+12099209800', 
                                         body='Hari ini hujan, jangan lupa bawa payung', 
                                         to='+6281215695656')

print(message.sid)