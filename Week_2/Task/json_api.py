# Json API(call using api to get data in json(data fromat) form)
import requests

session = requests.Session()

city = input("Enter City to Calculate the Risk : ")

para = {
    "key": "1c4f42d71cf245f3a6a55200261505",
    "q": city
}

try:
    response = session.get("http://api.weatherapi.com/v1/current.json",params=para)

    full = response.json()
    data = full['location']
    current = full['current']

    name = data['name']
    region = data['region']
    time = data['localtime']

    temp = current['temp_c']
    wind = current['wind_kph']
    wind_dir = current['wind_dir']
    condition = current["condition"]["text"]
    icon= current["condition"]["icon"]
    humidity = current["humidity"]
    chance = current['chance_of_rain']
    uv = current['uv']



    print(f"Name : {name}")
    print(f"Region : {region}")
    print(f"Time : {time}")
    print(f"Temperature : {temp}")
    print(f"Humidity : {humidity}")
    print(f"Chance of Rain : {chance}")
    print(f"Wind Speed : {wind}")
    print(f"Wind Direction : {wind_dir}")
    print(f"Ultravoilet Rays : {uv}")
    print(f"Weather Type : {condition}")
    print(f"Weather Icon : {icon}")

except Exception as e:
    print(f"Error Ocurred : {e}")

