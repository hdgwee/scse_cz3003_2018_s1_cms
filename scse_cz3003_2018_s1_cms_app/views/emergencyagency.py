from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.core import serializers
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt

import requests
from django.shortcuts import render
from scse_cz3003_2018_s1_cms_app.models import CrisisLevel, IncidentReport, Source
from decimal import Decimal
import json
import datetime
from django.utils import timezone
import json
from django.core.mail import send_mail
from django.conf import settings
from django.template import loader
from firebase import firebase
from datetime import date, timedelta
from scse_cz3003_2018_s1_cms_app.views.login import verifyRole


#########################################################################
# views
#########################################################################

def updatestatus_notification(request):
    res, role = verifyRole(request, ['er'])
    if res != 'success':
        return res
    all_incident_reports = IncidentReport.objects.values()
    all_unseen_reports = all_incident_reports.filter(validated='unseen')
    if len(all_unseen_reports) == 0:
        return render(request, 'reports/allincidentreport_validated.html')
    ir = all_unseen_reports[0]
    ir_formatted = {}
    ir_formatted['ReportID'] = ir['id']
    ir_formatted['Crisis Level'] = CrisisLevel.objects.get(id=ir['crisis_level_id']).name
    ir_formatted['Description'] = ir['description']
    dt = ir['date_time']
    ir_formatted['Date and Time'] = dt.strftime("%d %B %Y %I:%M%p")
    ir_formatted['Longitude'] = str(ir['longitude'])
    ir_formatted['Latitude'] = str(ir['latitude'])
    ir_formatted['Unit Number'] = ir['unit_number']
    ir_formatted['Street'] = ir['street']
    ir_formatted['Postal Code'] = ir['postal_code']
    ir_formatted['Phone Operator'] = Source.objects.get(id=ir['source_id']).name
    ir_formatted['Name'] = ir['name']
    ir_formatted['Mobile Number'] = str(ir['mobile_number'])

    return render(request, 'emergencyresponse/updatestatus_notification.html', {
        'page_name': 'Update Status for Emergency Notification',
        'incident_report': ir_formatted
    })