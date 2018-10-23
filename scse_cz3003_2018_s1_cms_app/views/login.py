from django.views.decorators.csrf import csrf_exempt
import requests
from django.shortcuts import render
from django.http import HttpResponse, Http404


########################################################################################################################
# Views
########################################################################################################################


def login(request):
    return render(request, 'login.html')


def home(request):
    return render(request, 'home.html', {'page_name': "Homepage"})



########################################################################################################################
# APIs
########################################################################################################################

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

            print('session_cookie', session_cookie.text[:10])
            if not (session_cookie.text == 'error'):
                print('creating session')
                response = HttpResponse("successful")

                response.set_cookie('auth', session_cookie.text)

                print("session created")

                return home(request)
        except Exception:
            return HttpResponse("fail")
    else:
        return HttpResponse("fail")



