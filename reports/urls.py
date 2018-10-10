from django.urls import path

from . import views


app_name = 'reports'
urlpatterns = [
    path('create/', views.create_incidentreport, name='create_incidentreport'),
    path('status/', views.generate_statusreport, name='generate_statusreport'),
    path('validate/', views.validate_incidentreport, name='validate_incidentreport'),
    # APIs
    path('submit_statusreports/', views.submit_statusreports, name = 'submit_statusreports'),
    path('add_incidentreport/', views.add_incidentreport, name='add_incidentreport'),
    path('submit_validationresponse/', views.submit_validationresponse, name='submit_validationresponse'),
    path('submit_invalidation/', views.submit_invalidation, name='submit_invalidation'),

]