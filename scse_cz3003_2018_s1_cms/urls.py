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

    #incident reports start here

    # path('reports/', include('reports.urls'))

    path('reports/create/', views.create_incidentreport, name='create_incidentreport'),

    path('reports/status/', views.generate_statusreport, name='generate_statusreport'),

    path('reports/validate/', views.validate_incidentreport, name='validate_incidentreport'),
    # APIs
    path('reports/submit_statusreports/', views.submit_statusreports, name = 'submit_statusreports'),

    path('reports/add_incidentreport/', views.add_incidentreport, name='add_incidentreport'),

    path('reports/submit_validationresponse/', views.submit_validationresponse, name='submit_validationresponse'),

    path('reports/submit_invalidation/', views.submit_invalidation, name='submit_invalidation'),

    path('reports/get_allincidentreport/', views.get_allincidentreport, name ='get_allincidentreport')

]
