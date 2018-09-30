from django.http import JsonResponse, HttpResponse

from scse_cz3003_2018_s1_cms_app.models import PublicServiceAnnouncement


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
