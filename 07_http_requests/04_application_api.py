import requests

url = "http://api.weatherapi.com/v1/current.json"
key = "0b239a0da9a549a98e9160230230811"

location = input("location : ")

response = requests.get(url, params = {
    "key": key,
    "q": location,
    "lang": "en"
})

result = response.json()
city = result["location"]["name"]
weather = result["current"]["temp_c"]
text = result["current"]["condition"]["text"]

print(f"{city} it's {weather} degrees Celsius right now and {text}")