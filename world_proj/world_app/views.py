from django.shortcuts import render
from .models import City, Country, Countrylanguage
from .admin import cityAdmin,countryAdmin,countrylanguageAdmin

def index(request):
    city=City.objects.all()
    country=Country.objects.all()
    countrylanguage=Countrylanguage.objects.all()
    city_attributes=cityAdmin.list_display
    country_attributes=countryAdmin.list_display
    countrylanguage_attributes=countrylanguageAdmin.list_display
    query=request.GET.get('query')
    context={
        'city':city,
        'country':country,
        'countrylanguage':countrylanguage,
        'city_attributes':city_attributes,
        'country_attributes':country_attributes,
        'countrylanguage_attributes':countrylanguage_attributes,
        'query':query,
    }
    return render(request, 'world_app/index.html',context)
