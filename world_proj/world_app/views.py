from django.shortcuts import render
from .models import City, Country, Countrylanguage

def index(request):
    return render(request, 'world_app/index.html')
