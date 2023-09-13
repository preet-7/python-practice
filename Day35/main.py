import requests
import os
from twilio.rest import Client

account_sid = ""
auth_token = os.environ.get("AUTH_TOKEN")

OWN_Endpoint = "https://api.openweathermap.org/data/2.8/onecall"
api_key = os.environ.get("OWM_API_KEY")

weather_params = {
    "lat": 30.404626,
    "lon": 77.563795,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

will_rain = False
response = requests.get(OWN_Endpoint, params=weather_params)
response.raise_for_status()

weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella ",
        from_="",
        to="+919459111291"
    )
    print(message.status)
