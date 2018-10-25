from django.core import serializers
from django.db.models import Q
from django.http import HttpResponse, Http404
from django.shortcuts import render

from scse_cz3003_2018_s1_cms_app.connector.psi import get_psi_from_source
from scse_cz3003_2018_s1_cms_app.connector.dengue import get_dengue_info_from_source
from scse_cz3003_2018_s1_cms_app.models import PublicServiceAnnouncement


#######################################################################################################################
# Views
#######################################################################################################################

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


