from django.http import HttpResponse
from django.shortcuts import render

from scse_cz3003_2018_s1_cms_app.models import PublicServiceAnnouncement


def home(request):
    return render(request, 'home.html', {'page_name': "Homepage"})


def view_publicserviceannouncement(request):
    # try:
    #     publicServiceAnnouncement = PublicServiceAnnouncement.get(id=id)
    # except PublicServiceAnnouncement.DoesNotExist:
    #     raise Http404('PublicServiceAnnouncement not found')
    psa_list = PublicServiceAnnouncement.objects.all()
    return render(request, 'publicserviceannouncement/view_publicserviceannouncement.html',
                  {
                      'page_name': "Manage Public Service Announcement",
                      'psa_list': psa_list
                  })


def new_publicserviceannouncement(request):
    # try:
    #     publicServiceAnnouncement = PublicServiceAnnouncement.get(id=id)
    # except PublicServiceAnnouncement.DoesNotExist:
    #     raise Http404('PublicServiceAnnouncement not found')

    return render(request, 'publicserviceannouncement/new_publicserviceannouncement.html',
                  {'page_name': "New Public Service Announcement"})


def add_publicserviceannouncement(request):
    if request.method == 'POST':
        try:
            title = request.POST.get('title')
            description = request.POST.get('description')
        except KeyError:
            return HttpResponse('unsuccessful')
        else:
            publicserviceannouncement = PublicServiceAnnouncement()
            publicserviceannouncement.title = title
            publicserviceannouncement.description = description
            publicserviceannouncement.save()
            return HttpResponse('successful')
