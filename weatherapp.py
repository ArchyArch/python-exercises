import requests

city = 'London'
url = f'http://api.openweathermap.org/data/2.5/forecast?q=London&appid=767573953473bdb871a80111df8b19af&units=metric'

forecasts = requests.get(url).json()

for forecast in forecasts['list']:
    temperature = round(forecast['main']['temp'])
    weather_description = forecast['weather'][0]['description']
    cloudiness = forecast['clouds']['all']
    message = f"Today's weather for {city}\n🌡️️: {temperature} °C\n🌤️: {weather_description}\n☁️: {cloudiness}%"
    print(message)
