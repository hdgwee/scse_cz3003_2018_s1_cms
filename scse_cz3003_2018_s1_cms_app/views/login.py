from django.views.decorators.csrf import csrf_exempt
import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404


def verifyRole(view):
    def executeView(*args, **kwargs):
        result = view(*args, **kwargs)
        request = args[0]
        if 'role' in kwargs.keys():
            role = kwargs['role']
        else:
            role = 'cms'
        cookie = request.COOKIES.get('auth')
        dictToSend = {
            'cookie': cookie
        }
        authenticatedRole = requests.post('http://localhost:5002/checkCookie', json=dictToSend)
        print('role:', authenticatedRole.text)
        if role != authenticatedRole.text:
            print('incorrect role')
            return HttpResponse('You do not have permission to access this webpage')
        else:
            return result
    return executeView

########################################################################################################################
# Views
########################################################################################################################


def login(request):
    return render(request, 'login.html')


@verifyRole
def home(request):
    return render(request, 'home.html', {'page_name': "Homepage"})


########################################################################################################################
# APIs
########################################################################################################################

@csrf_exempt
def authorization(request):
    if request.method == 'POST':
        # try:
            # Log the user in
        dictToSend = {
            'username': request.POST.get('username'),
            'password': request.POST.get('password')
        }
        session_cookie = requests.post('http://localhost:5002/login', json=dictToSend)
        print('session_cookie', session_cookie.text[:10])
        if not (session_cookie.text == 'error'):
            # response = HttpResponse("successful")
            response = redirect('home')
            response.set_cookie('auth', session_cookie.text)
            return response
        # except Exception:
        #     return HttpResponse("fail")
    return HttpResponse("fail")



