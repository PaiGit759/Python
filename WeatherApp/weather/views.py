import requests
from django.shortcuts import render
from .models import City
from .form import CityForm

def index(request):

    appid = 'f7be37d83805eb36febf406de33bd7f9'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={},&units=metric&appid=' + appid
    message = ''

    if(request.method == 'POST' ) :
        res = requests.get(url.format(request.POST['name'])).json()

        if(res['cod'] == 200 ) :
            form = CityForm(request.POST)
            form.save()
            message = 'City added to database'
        else : 
            #print(res['cod'],'^^^^^ : Error')
            message = 'There is no such city'

    form = CityForm()

    cityis = City.objects.all()
    all_cityis = []
    all_cityis1 = []


    for city in cityis :
        res = requests.get(url.format(city.name)).json()

        if(res['cod'] == 200 ) :
        #    print(res['cod'])
        #   print(res['sys']['cod'])


            city_info = {
                'city': city.name,
                'temp': res['main']['temp'],
                'icon': res['weather'][0]['icon'],
            }
            all_cityis.append(city_info)
        else : continue    


    context = {'all_info': all_cityis, 'form': form, 'message' : message}

    return render(request, 'weather/index.html', context)
