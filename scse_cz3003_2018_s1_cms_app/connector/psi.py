import requests
import json
import datetime


from scse_cz3003_2018_s1_cms_app.models import Psi, PsiType
from decimal import *
from django.http import JsonResponse


def get_psi_from_source():
    url = 'https://api.data.gov.sg/v1/environment/psi'
    response = requests.get(url)

    if response.ok:
        json_data = json.loads(response.content)

        # Get 24 hours reading and save it into database
        if Psi.objects.filter(date_time=json_data['items'][0]['update_timestamp']
                , type__machine_readable_name__exact="psi_twenty_four_hourly").count() == 0:
            psi = Psi()
            psi.national = Decimal(json_data['items'][0]['readings']['psi_twenty_four_hourly']['national'])
            psi.north = Decimal(json_data['items'][0]['readings']['psi_twenty_four_hourly']['north'])
            psi.south = Decimal(json_data['items'][0]['readings']['psi_twenty_four_hourly']['south'])
            psi.east = Decimal(json_data['items'][0]['readings']['psi_twenty_four_hourly']['east'])
            psi.west = Decimal(json_data['items'][0]['readings']['psi_twenty_four_hourly']['west'])
            psi.central = Decimal(json_data['items'][0]['readings']['psi_twenty_four_hourly']['central'])
            psi.type = PsiType.objects.get(machine_readable_name='psi_twenty_four_hourly')
            psi.date_time = json_data['items'][0]['update_timestamp']
            psi.save()

        # Get PM 2.5 reading and save it into database
        if Psi.objects.filter(date_time=json_data['items'][0]['update_timestamp']
                , type__machine_readable_name__exact="pm25_twenty_four_hourly").count() == 0:
            psi_25 = Psi()
            psi_25.national = Decimal(json_data['items'][0]['readings']['pm25_twenty_four_hourly']['national'])
            psi_25.north = Decimal(json_data['items'][0]['readings']['pm25_twenty_four_hourly']['north'])
            psi_25.south = Decimal(json_data['items'][0]['readings']['pm25_twenty_four_hourly']['south'])
            psi_25.east = Decimal(json_data['items'][0]['readings']['pm25_twenty_four_hourly']['east'])
            psi_25.west = Decimal(json_data['items'][0]['readings']['pm25_twenty_four_hourly']['west'])
            psi_25.central = Decimal(json_data['items'][0]['readings']['pm25_twenty_four_hourly']['central'])
            psi_25.type = PsiType.objects.get(machine_readable_name='pm25_twenty_four_hourly')
            psi_25.date_time = json_data['items'][0]['update_timestamp']
            psi_25.save()


def get_psi(request):
    if request.method == 'GET':
        psi_type = request.GET['psi_type']

        # http://127.0.0.1:8080/get_psi?psi_type=psi_twenty_four_hourly
        if psi_type == "psi_twenty_four_hourly":
            psi = Psi.objects.order_by('-date_time')\
                .filter(type__machine_readable_name__exact='psi_twenty_four_hourly').first()

            if psi is not None:
                return JsonResponse(
                    {
                        'national': psi.national,
                        'north': psi.north,
                        'south': psi.south,
                        'east': psi.east,
                        'west': psi.west,
                        'central': psi.central,
                        'type': psi.type.human_readable_name,
                        'time': str(psi.date_time.timestamp())[:-2]
                    }
                )

        # http://127.0.0.1:8080/get_psi?psi_type=pm25_twenty_four_hourly
        elif psi_type == "pm25_twenty_four_hourly":
            psi = Psi.objects.order_by('-date_time')\
                .filter(type__machine_readable_name__exact='pm25_twenty_four_hourly').first()

            if psi is not None:
                return JsonResponse(
                    {
                        'national': psi.national,
                        'north': psi.north,
                        'south': psi.south,
                        'east': psi.east,
                        'west': psi.west,
                        'central': psi.central,
                        'type': psi.type.human_readable_name,
                        'time': str(psi.date_time.timestamp())[:-2]
                    }
                )

    return JsonResponse('', safe=False)
