from django.views.decorators.csrf import csrf_exempt
import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib import messages

def verifyRole(request, role):
    #role = 'cms' 'pmo' 'er' 'po'
    # pmo @ singapore.com
    # cmsoperator @ singapore.com
    # emergencyresponse @ singapore.com
    cookie = request.COOKIES.get('auth')
    dictToSend = {
        'cookie': cookie
    }
    authenticatedRole = requests.post('http://localhost:5002/checkCookie', json=dictToSend)
    print('role:', authenticatedRole.text)
    if authenticatedRole.text == 'error':
        messages.warning(request, 'You are not authorised to visit that page. Please login again.')
        response = redirect('login')
        return response, authenticatedRole.text
    else:
        if authenticatedRole.text not in role:
            messages.warning(request, 'You are not authorised to visit that page. Please login again.')
            response = redirect('login')
            return response, authenticatedRole.text
        else:
            return 'success', authenticatedRole.text

########################################################################################################################
# Views
########################################################################################################################


def login(request):
    return render(request, 'login.html')


def home(request):
    res, role = verifyRole(request, ['cms', 'po'])
    if res != 'success':
        return res
    if role == 'po':
        return render(request, 'reports/create_incidentreport.html', {'page_name': "Homepage"})
    else:
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



