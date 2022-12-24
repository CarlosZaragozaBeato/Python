from django.shortcuts import render
from django.http import HttpResponse

from .models import Place,Restaurant
def create(request):
    
    place = Place(name="Lugar14", address="Call1")
    place.save()
    
    restaurant = Restaurant(place = place)
    restaurant.save()
    
    return HttpResponse(restaurant.place.name)
