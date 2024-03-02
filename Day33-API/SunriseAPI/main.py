import requests
import datetime as dt

parameter = {
    'lat' : -6.175247,
    'lng' : 106.827049,
    'formatted' : 0,
    'tzid' : 'Asia/Jakarta'
}

response = requests.get(url = 'https://api.sunrise-sunset.org/json', params=parameter)

sunrise = response.json()['results']['sunrise'].split('T')[1].split(':')[0]

