#import module
import requests

#acii
a = '''
 +-++-++-++-+ +-++-+ +-++-++-++-++-++-++-+ +-++-++-++-++-+
 |c||o||d||e| |b||y| |M||a||n||s||o||o||r| |B||a||r||r||i|
 +-++-++-++-+ +-++-+ +-++-++-++-++-++-++-+ +-++-++-++-++-+
'''

#print ascii
print(a)

#set your api key
API_KEY = "f34c41d86485338a343c2ffa5b0971d5"

#set base URL
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

#take input about the city
city = input("Enter a city name: ")

#set url to request
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"

#request the url. set the reponse
response = requests.get(request_url)

#print the data if status code is 200 other wise print 'error'
if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] - 273.15, 2)

    print("Weather:", weather)
    print("Temperature:", temperature, "celsius")
else:
    print("An error occurred.")
