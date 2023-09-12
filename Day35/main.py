import requests

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = ""

weather_params = {
    "lat": 30.404626,
    "lon": 77.563795,
    "appid": api_key,
}

response = requests.get(OWN_Endpoint, params=weather_params)
print(response.json())