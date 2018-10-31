import datetime
import os
import shutil
import time
import xml.etree.ElementTree
import zipfile
from django.http import HttpResponse, Http404
import json

import requests
from django.http import JsonResponse

from scse_cz3003_2018_s1_cms_app.models import Dengue


def get_dengue_info_from_source():
    cur_time = str(int(time.time()))
    file_name = cur_time + '_dengue.zip'
    folder_name = cur_time + '_dengue'

    # Get zip file from url
    url = 'http://storage.data.gov.sg/dengue-clusters/dengue-clusters.zip'
    r = requests.get(url)
    with open(file_name, 'wb') as outfile:
        outfile.write(r.content)

    # Extract zip file
    zip_ref = zipfile.ZipFile(file_name, 'r')
    zip_ref.extractall(folder_name)
    zip_ref.close()

    # Process
    root = xml.etree.ElementTree.parse(folder_name + '/dengue-clusters-kml.kml').getroot()

    for i in range(len(root[0][3])):
        if i > 0:
            unformatted_dengue_date_time = root[0][3][i][3][0][5].text
            formatted_dengue_date_time = datetime.datetime.strptime(unformatted_dengue_date_time, '%Y%m%d%H%M%S')

            coordinates = root[0][3][i][4][0][0][0].text
            coordinate = coordinates.split(' ')[0]

            latlng = coordinate.split(',')
            cur_lng = latlng[0]
            cur_lat = latlng[1]

            if Dengue.objects.filter(date_time=formatted_dengue_date_time, lat=cur_lat, lng=cur_lng).count() == 0:
                dengue = Dengue()
                dengue.lat = cur_lat
                dengue.lng = cur_lng
                dengue.date_time = formatted_dengue_date_time
                dengue.save()

    # Remove downloaded files
    os.remove(file_name)
    shutil.rmtree(folder_name)


# http://127.0.0.1:8080/get_dengue_info
def get_dengue_info(request):
    if request.method == 'GET':
        dengues = Dengue.objects.order_by('-date_time').all()

        response = []
        
        for dengue in dengues:
            dengue_incident = {}
            dengue_incident["date_time"] = str(dengue.date_time.timestamp())[:-2]
            dengue_incident["lat"] = str(dengue.lat)
            dengue_incident["lng"] = str(dengue.lng)
            response.append(dengue_incident)
            

        return HttpResponse(json.dumps(response), content_type='application/json')

    return HttpResponse(json.dumps(''), content_type='application/json')
