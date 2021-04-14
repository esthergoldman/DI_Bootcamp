import requests
from django.shortcuts import render


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=e2fd99743e43e679394b7a7882817008'
    city ="Tel Aviv"

    r = requests.get(url.format(city)).json()
    print(r.text)

        city_weather = {
            'city' : city.name,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }

    return render(request, 'index.html')