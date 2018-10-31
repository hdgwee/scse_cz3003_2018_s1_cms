from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from firebase import firebase
import json
from django.views.decorators.csrf import csrf_exempt
temp = firebase.FirebaseApplication('https://testapp-ab172.firebaseio.com/', None)

def notification_read(request):
    key = request.GET.get("tag", "no_key")
    if "no_key" in key:
        print("No Key Detected")
        return HttpResponseRedirect('/')
    result = temp.get('/notification', key)
    print(result['message'])
    print(result['title'])
    print(result['twitter'])
    print(result['facebook'])
    print(result['sms'])

    sms = int(result['sms'])
    facebook = int(result['facebook'])
    twitter = int(result['twitter'])
    if sms == 1:
        sms = "Yes"
    else:
        sms = "No"

    if facebook == 1:
        facebook = "Yes"
    else:
        facebook = "No"

    if twitter == 1:
        twitter = "Yes"
    else:
        twitter = "No"

    return render(request, 'publicserviceannouncement/view_psanotification.html',
                  {
                      'page_name': "View Notification",
                      'message': result['message'],
                      'message_title': result['title'],
                      'facebook': facebook,
                      'twitter': twitter,
                      'sms': sms
                   })

def deletenotification(request):
    if request.method == 'POST':
        try:
            key = request.POST.get("key")
        except KeyError:
            return HttpResponse('unsuccessful')
        else:
            temp.delete('/notification', key)

    return HttpResponse('successful')

@csrf_exempt
def psamessagefrompmo(request):
    json_dict = json.loads(request.body)
    title = json_dict["title"]
    message = json_dict["message"]
    fb = json_dict["facebook"]
    twitter = json_dict["twitter"]
    sms = json_dict["sms"]
    #print(title)
    #print(message)
    #print(fb)
    #print(sms)
    result = temp.post('/notification',
                       data={
                           "title": title,
                           "message": message,
                           "facebook": fb,
                           "sms": sms,
                           "twitter": twitter},
                       params={'print': 'pretty'})

    print(result)
    return HttpResponse('Success')
