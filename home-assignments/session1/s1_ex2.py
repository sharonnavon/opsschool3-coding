#!/usr/bin/env python3

import requests

location_by_ip_api = 'http://ip-api.com/json'
weather_api = 'http://api.openweathermap.org/data/2.5/weather?q={city},{country}&APPID=0cc0ca27e7ece98aff5593433c6d082a'

r = requests.get(location_by_ip_api)

r.json()

