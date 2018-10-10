from django.contrib import admin
from django.urls import path, include

from scse_cz3003_2018_s1_cms_app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    ###################################################################################################################
    # Views
    path('', views.home, name='home'),
    
    path('view_publicserviceannouncement', views.view_publicserviceannouncement
         , name='view_publicserviceannouncement'),

    path('new_publicserviceannouncement', views.new_publicserviceannouncement
         , name='new_publicserviceannouncement'),

    path('edit_publicserviceannouncement/<int:id>', views.edit_publicserviceannouncement
         , name='edit_publicserviceannouncement'),

    ###################################################################################################################
    # HTTP POST Requests
    path('add_publicserviceannouncement', views.add_publicserviceannouncement
         , name='add_publicserviceannouncement'),

    path('update_publicserviceannouncement', views.update_publicserviceannouncement
         , name='update_publicserviceannouncement'),

    path('delete_publicserviceannouncement', views.delete_publicserviceannouncement
         , name='delete_publicserviceannouncement'),

    path('get_all_reusable_publicserviceannouncement', views.get_all_reusable_publicserviceannouncement
         , name='get_all_reusable_publicserviceannouncement'),

    path('reports/', include('reports.urls'))

]
