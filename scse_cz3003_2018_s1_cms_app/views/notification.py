from django.http import HttpResponseRedirect, HttpResponse
from firebase import firebase
import json
from django.views.decorators.csrf import csrf_exempt
temp = firebase.FirebaseApplication('https://testapp-ab172.firebaseio.com/', None)

def notification_read(request):
    key = request.GET.get("tag", "no_key")
    if "no_key" in key:
        print("No Key Detected")
        return HttpResponseRedirect('/')
    else:
        print("Hi")
    result = temp.get('/notification', key)
    print(result)
    temp.delete('/notification', key)
    return HttpResponseRedirect('/new_publicserviceannouncement')

@csrf_exempt
def psamessagefrompmo(request):
    json_dict = json.loads(request.body)
    title = json_dict["title"]
    message = json_dict["message"]
    print(title)
    print(message)
    new_user = "tp8rGGD37PfAaqnmaI8ncvc0MnQ2"
    #result = temp.post('/notification', new_user, {'print': 'pretty'}, {'X_FANCY_HEADER': 'VERY FANCY'})
    result = temp.post('/notification', data={"title": title , "message": message}, params={'print': 'pretty'})
    print(result)
    return HttpResponse('Success')
