import json
import html
import pandas as pd
import requests

# storing API key in code is considered bad practice
# you should never share your API key with anyone or make it puclicly available 
api_key = "MroGw5CAFMBarkIhJYSAauFEKqScAAbi"

url = "http://www.mapquestapi.com/directions/v2/route"
url += "?key=" + api_key
url += "&from=Pho Quang,Tan Binh District,Ho Chi Minh City&to=Ly Tu Trong,District 1,Ho Chi Minh City"
# ? starts the query string
# = seperates the key from (search terms)

print(url)

# print out route distance and time
response = requests.get(url=url)
json_obj = json.loads(response.text)
route_obj = json_obj["route"]
distance = route_obj["distance"]
time = route_obj["formattedTime"]
print(distance)
print(time)