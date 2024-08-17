from django.shortcuts import render
from django.http import JsonResponse
import requests
import os

# Create your views here.


def get_weather(request):
    city = request.GET.get('city')
    api_key = os.getenv('OPENWEATHER_API_KEY')
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = request.get(url)
    weather_data = response.json()
    return JsonResponse(weather_data)

