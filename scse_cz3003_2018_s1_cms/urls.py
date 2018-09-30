from django.contrib import admin
from django.urls import path, include, re_path

from scse_cz3003_2018_s1_cms_app.views import base_views, response

urlpatterns = [
    path('admin/', admin.site.urls),

    # View
    path('', base_views.home, name='home'),
    
    path('view_publicserviceannouncement', base_views.view_publicserviceannouncement
         , name='view_publicserviceannouncement'),

    path('new_publicserviceannouncement', base_views.new_publicserviceannouncement
         , name='new_publicserviceannouncement'),

    # HTTP POST Request
    path('add_publicserviceannouncement', response.add_publicserviceannouncement
         , name='add_publicserviceannouncement')
]
