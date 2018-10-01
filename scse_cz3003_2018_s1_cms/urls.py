from django.contrib import admin
from django.urls import path

from scse_cz3003_2018_s1_cms_app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Views
    path('', views.home, name='home'),
    
    path('view_publicserviceannouncement', views.view_publicserviceannouncement
         , name='view_publicserviceannouncement'),

    path('new_publicserviceannouncement', views.new_publicserviceannouncement
         , name='new_publicserviceannouncement'),

    # HTTP POST Requests
    path('add_publicserviceannouncement', views.add_publicserviceannouncement
         , name='add_publicserviceannouncement')
]
