import requests
from twilio.rest import Client

account_sid = 'AC4ec3f5cf84dc376207713b376c960fd7'
auth_token = '2a4be6e56fc1081f5a73bb2fe4736c23'
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