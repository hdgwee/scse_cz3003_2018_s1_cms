import os
import requests
import json
from datetime import date
from django.http import JsonResponse

def get_weather(request):
    today = str(date.today())
    strURL = 'https://api.data.gov.sg/v1/environment/2-hour-weather-forecast?date='+today
    print(strURL)
    response = requests.get(strURL)
    geodata = response.json()

    data = {
        'east': geodata['items'][0]['forecasts'][9]['forecast'],
        'west': geodata['items'][0]['forecasts'][6]['forecast'],
        'north': geodata['items'][0]['forecasts'][32]['forecast'],
        'south': geodata['items'][0]['forecasts'][12]['forecast'],
        'central': geodata['items'][0]['forecasts'][2]['forecast']
    }
    return JsonResponse(data)
