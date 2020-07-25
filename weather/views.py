from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=?';
    city="Indore"
    if request.method=="POST":
        city=request.POST['city']
    #print("Vishal")
    #print(city)
    r=requests.get(url.format(city)).json();
    city_temp={
        'city':city,
        'logo':r['weather'][0]['icon'],
        'temp':r['main']['temp'],
        'pressure':r['main']['pressure'],
        'humidity':r['main']['humidity'],
        'desc':r['weather'][0]['description']
    }
    context={'city_temp':city_temp}
    print(r)
    return render(request,'weather/weather.html',context)
