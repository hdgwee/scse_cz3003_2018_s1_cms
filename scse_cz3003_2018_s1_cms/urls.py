from django.contrib import admin
from django.urls import path

from scse_cz3003_2018_s1_cms_app.views import reports, announcements, login, notification, emergencyagency
from scse_cz3003_2018_s1_cms_app.connector import psi, dengue

urlpatterns = [
    path('admin/', admin.site.urls),
    ###################################################################################################################
    # Views
    path('home', login.home, name='home'),

    path('', login.login, name='login_other'),

    path('view_publicserviceannouncement', announcements.view_publicserviceannouncement
         , name='view_publicserviceannouncement'),

    path('publish_publicserviceannouncement', announcements.publish_publicserviceannouncement
         , name='publish_publicserviceannouncement'),

    path('new_publicserviceannouncement', announcements.new_publicserviceannouncement
         , name='new_publicserviceannouncement'),

    path('edit_publicserviceannouncement/<int:id>', announcements.edit_publicserviceannouncement
         , name='edit_publicserviceannouncement'),

    ###################################################################################################################
    # HTTP POST Requests
    path('add_publicserviceannouncement', announcements.add_publicserviceannouncement
         , name='add_publicserviceannouncement'),

    path('update_publicserviceannouncement', announcements.update_publicserviceannouncement
         , name='update_publicserviceannouncement'),

    path('delete_publicserviceannouncement', announcements.delete_publicserviceannouncement
         , name='delete_publicserviceannouncement'),

    path('get_all_reusable_publicserviceannouncement', announcements.get_all_reusable_publicserviceannouncement
         , name='get_all_reusable_publicserviceannouncement'),

    # Incident reports start here

    # path('reports/', include('reports.urls'))

    path('reports/create/', reports.create_incidentreport, name='create_incidentreport'),

    path('reports/status/', reports.generate_statusreport, name='generate_statusreport'),

    path('reports/validate/', reports.validate_incidentreport, name='validate_incidentreport'),
    # APIs
    path('reports/submit_statusreports/', reports.submit_statusreports, name='submit_statusreports'),

    path('reports/add_incidentreport/', reports.add_incidentreport, name='add_incidentreport'),

    path('reports/submit_validationresponse/', reports.submit_validationresponse, name='submit_validationresponse'),

    path('reports/submit_invalidation/', reports.submit_invalidation, name='submit_invalidation'),

    path('reports/get_allincidentreport/', reports.get_allincidentreport, name ='get_allincidentreport'),

    path('login/', login.login, name='login'),

    path('authorization/', login.authorization, name='authorization'),

    #=====Emergency=====#

    path('notification/', emergencyagency.updatestatus_notification, name='updatestatusofemergencynotification'),

    #=====Notification=====#
    path('notification_read', notification.notification_read, name='notificationRead'),

    path('psamessagefrompmo', notification.psamessagefrompmo, name='psamessagefrompmo'),

    path('deletenotification', notification.deletenotification, name="deletenotification"),

    # =====Scheduler=====#
    path('reports/send_email', reports.send_email, name='send_email'),

    # =====SMS=====#
    path('announcements/sms', announcements.sms, name="sns"),

    #=====Crawled Data=====#
    path('get_psi', psi.get_psi, name='get_psi'),

    path('get_dengue_info', dengue.get_dengue_info, name='get_dengue_info')
]
