import requests
import os
import json

city = input("Enter the name of the city\n")

url = f"http://api.weatherapi.com/v1/current.json?key=d6309222b672421faca83112231805&q={city}"

r = requests.get(url)
#print(r.text)

wdic = json.loads(r.text)
w = (wdic["current"]["temp_c"])

os.system(f"say 'the weather in {city} is {w} degrees celsius' ")

