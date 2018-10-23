from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.core import serializers
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from scse_cz3003_2018_s1_cms_app.models import PublicServiceAnnouncement
import requests

#######################################################################################################################
# Views
#######################################################################################################################
def home(request):
    return render(request, 'home.html', {'page_name': "Homepage"})


def view_publicserviceannouncement(request):
    psa_list = PublicServiceAnnouncement.objects.all().filter(reusable=True)
    return render(request, 'publicserviceannouncement/view_publicserviceannouncement.html',
                  {
                      'page_name': "Manage Public Service Announcement",
                      'psa_list': psa_list
                  })


def new_publicserviceannouncement(request):
    return render(request, 'publicserviceannouncement/new_publicserviceannouncement.html',
                  {'page_name': "New Public Service Announcement"})


def edit_publicserviceannouncement(request, id):
    try:
        psa = PublicServiceAnnouncement.objects.get(pk=id)
    except PublicServiceAnnouncement.DoesNotExist:
        raise Http404('PublicServiceAnnouncement not found')
    return render(request, 'publicserviceannouncement/edit_publicserviceannouncement.html',
                  {
                      'page_name': "Edit Public Service Announcement",
                      'psa': psa
                  })


#######################################################################################################################
# HTTP POST Requests
#######################################################################################################################
def add_publicserviceannouncement(request):
    if request.method == 'POST':
        try:
            title = request.POST.get('title')
            description = request.POST.get('description')
        except KeyError:
            return HttpResponse('unsuccessful')
        else:
            psa = PublicServiceAnnouncement()
            psa.title = title
            psa.description = description
            psa.reusable = True
            psa.save()
            return HttpResponse('successful')


def update_publicserviceannouncement(request):
    if request.method == 'POST':
        try:
            id = request.POST.get('id')
            title = request.POST.get('title')
            description = request.POST.get('description')
        except KeyError:
            return HttpResponse('unsuccessful')
        else:
            psa = PublicServiceAnnouncement.objects.get(pk=id)
            psa.title = title
            psa.description = description
            psa.save()
            return HttpResponse('successful')


def delete_publicserviceannouncement(request):
    if request.method == 'POST':
        try:
            id = request.POST.get('id')
        except KeyError:
            return HttpResponse('unsuccessful')
        else:
            psa = PublicServiceAnnouncement.objects.get(pk=id)
            psa.reusable = False
            psa.save()

            return HttpResponse('successful')


def get_all_reusable_publicserviceannouncement(request):
    if request.method == 'POST':
        try:
            keyword = request.POST.get('keyword')
        except KeyError:
            return HttpResponse('unsuccessful')
        else:
            return HttpResponse(serializers.serialize('json' , PublicServiceAnnouncement.objects.all()
                                                      .filter(Q(title__contains=keyword) | Q(description__contains=keyword))
                                                      .filter(reusable=True)
                                                      , fields=('id', 'title', 'description'))
                                , content_type="application/json")
    elif request.method == 'GET':
        return HttpResponse(serializers.serialize('json'
                                                  , PublicServiceAnnouncement.objects.all().filter(reusable=True)
                                                  , fields=('id', 'title', 'description'))
                            , content_type="application/json")




#start of incident report
from django.shortcuts import render
from django.http import HttpResponse, Http404
from scse_cz3003_2018_s1_cms_app.models import CrisisLevel, IncidentReport, Source, StatusReport
from decimal import Decimal
import json
import datetime
from pytz import timezone
import json


# TODO: figure out how to implement the date filter function in generate status report, link up with emergency response, figure out if the fiekds for incident report are correct


def create_incidentreport(request):

    crisis_level = CrisisLevel.objects.all()
    return render(request, 'reports/create_incidentreport.html',
                  {'page_name': "Create Incident Report",
                   'crisis_level': crisis_level
                   })


def generate_statusreport(request):
    all_incident_reports = IncidentReport.objects.values()

    for ir in all_incident_reports:
        dt = ir['date_time']
        # Pass a date to the ir so that it can be hidden
        ir['date'] = dt.strftime("%Y-%m-%d")

        ir['date_time'] = dt.strftime("%Y %B %d %I:%M%p")
        ir['mobile_number'] = str(ir['mobile_number'])
        ir['longitude'] = str(ir['longitude'])
        ir['latitude'] = str(ir['latitude'])
        ir['crisis_level_id'] = CrisisLevel.objects.get(id=ir['crisis_level_id']).name
        ir['source_id'] = Source.objects.get(id=ir['source_id']).name

    return render(request, 'reports/generate_statusreports.html', {
        'page_name': 'Generate Status Reports',
        'all_incident_reports': all_incident_reports

    })

################################# api for pmo ######################################
@csrf_exempt
def get_allincidentreport(request):
    all_incident_reports = IncidentReport.objects.values()

    for ir in all_incident_reports:
        dt = ir['date_time']
        # Pass a date to the ir so that it can be hidden
        ir['date'] = dt.strftime("%Y-%m-%d")

        ir['date_time'] = dt.strftime("%Y %B %d %I:%M%p")
        ir['mobile_number'] = str(ir['mobile_number'])
        ir['longitude'] = str(ir['longitude'])
        ir['latitude'] = str(ir['latitude'])
        ir['crisis_level_id'] = CrisisLevel.objects.get(id=ir['crisis_level_id']).name
        ir['source_id'] = Source.objects.get(id=ir['source_id']).name

    return HttpResponse(json.dumps(list(all_incident_reports)), content_type='application/json')

def validate_incidentreport(request):
    all_incident_reports = IncidentReport.objects.values()
    ir = all_incident_reports.filter(validated='unseen')[0]
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

    return render(request, 'reports/validate_incidentreport.html', {
        'page_name': 'Validate Incident Report',
        'incident_report': ir_formatted
    })

# Start of apis




def submit_invalidation(request):
    if request.method == 'POST':
        try:
            id = request.POST.get('id')
        except KeyError:
            return HttpResponse('unsuccessful')
        else:
            invalidated_report = IncidentReport.objects.get(id=id)
            invalidated_report.validated = 'invalid'
            invalidated_report.save()
            return HttpResponse('successful')


def submit_validationresponse(request):
    if request.method == 'POST':
        try:
            id = request.POST.get('id')
            scdf = request.POST.get('scdf')
            police = request.POST.get('police')
            gas = request.POST.get('gas')
            severity = request.POST.get('severity')
        except KeyError:
            return HttpResponse('unsuccessful')
        else:
            # send it to the database for emergency response
            validation = {}
            emergency_response = []
            if scdf:
                emergency_response.append('scdf')
            if police:
                emergency_response.append('police')
            if gas:
                emergency_response.append('gas')
            validation['emergency'] = emergency_response
            validation['severity'] = severity
            # update the incident report database
            validated_report = IncidentReport.objects.get(id=id)
            validated_report.validated = 'valid'
            validated_report.save()
            return HttpResponse('successful')


def submit_statusreports(request):
    if request.method == 'POST':
        try:
            reportIDs = request.POST.getlist('id[]')
        except KeyError:
            return HttpResponse('unsuccessful')
        else:
            sr = StatusReport()
            sr.date_time = datetime.datetime.now()
            sr.save()
            for reportID in reportIDs:
                in_rpt = IncidentReport.objects.get(id=reportID)
                sr.incident_report.add(in_rpt)
            return HttpResponse('successful')


def add_incidentreport(request):
    # figure out how to automatically add source
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            description = request.POST.get('description')
            mobile_number = request.POST.get('mobile_number')
            date = request.POST.get('date')
            time = request.POST.get('time')
            postal_code = request.POST.get('postal_code')
            unit_number = request.POST.get('unit_number')
            street = request.POST.get('street')
            longitude = request.POST.get('longitude')
            latitude = request.POST.get('latitude')
            crisis_level = request.POST.get('crisis_level')
            source = request.POST.get('source')

        except KeyError:
            return HttpResponse('unsuccessful')
        else:
            ir = IncidentReport()
            ir.name = name
            ir.description = description
            ir.mobile_number = int(mobile_number)

            date_ = date.split('-')
            year = int(date_[0])
            month = int(date_[1])
            day = int(date_[2])
            time_ = time.split(':')
            hour = int(time_[0])
            minute = int(time_[1])
            dt = datetime.datetime(year, month, day, hour, minute)
            ir.date_time = dt

            ir.postal_code = postal_code
            ir.unit_number = unit_number
            ir.street = street

            ir.longitude = Decimal(longitude)
            ir.latitude = Decimal(latitude)

            cl = CrisisLevel.objects.get(name=crisis_level)
            ir.crisis_level = cl
            src = Source.objects.get(name=source)
            ir.source = src

            ir.save()
            return HttpResponse('successful')


############################################################# login page ####################################

@csrf_exempt
def authorization(request):

    if request.method == 'POST':
        try:
            # Log the user in
            dictToSend = {
                'username': request.POST.get('username'),
                'password': request.POST.get('password')
            }
            print(dictToSend)
            session_cookie = requests.post('http://localhost:5002/login', json=dictToSend)

            print('session_cookie',session_cookie.text[:10])
            if not (session_cookie.text == 'error'):
                print('creating session')
                response = HttpResponse("successful")

                response.set_cookie('auth', session_cookie.text)

                print("session created")
                dictToSend = {
                    'cookie': session_cookie.text
                }
                role = requests.post('http://localhost:5002/checkCookie', json=dictToSend)
                print(role.text)
                return response
        except Exception:
            response = HttpResponse("fail")
            return response
    else:
        print("not a post")
    response = HttpResponse("fail")
    return response


def login(request):
    return render(request, 'login.html')