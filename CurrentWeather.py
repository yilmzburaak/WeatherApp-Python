import requests
import json

while True:

    city=input("Please enter the city you want to know the weather forecast for: ")

    apikey="--------------"
    apicall="https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(city,apikey)

    connect=requests.get(apicall)
    result=connect.json()

    weather=result["weather"][0]["description"]
    temperature=result["main"]["temp"]
    feltTemperature=result["main"]["feels_like"]
    pressure=result["main"]["pressure"]
    humidity=result["main"]["humidity"]


    print("\n\n---Weather information for {} is as follows---\n\nTemperature: {} °C\nWeather condition: {}\nThe felt temperature: {} °C\nPressure: {} hpa\nHumidity rate: {} %".format(city.capitalize(),temperature,weather,feltTemperature,pressure,humidity))