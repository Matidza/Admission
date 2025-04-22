
from django.urls import path
from . import views
#from .views import download_admission_form
app_name = 'application' 

urlpatterns = [
    path('', views.applications_summary, name='applications_summary'),
    path('applyadmission/<int:school_id>/', views.applyadmission, name='applyadmission'),
    
    path('applications_add/', views.applications_add, name='applications_add'),
    # Applictions Stuff
    path('application/<int:id>/', views.application, name='application'),
    path('update_application_status/<int:id>/', views.update_application_status, name='update_application_status'),
    path('update_application/<int:id>/', views.update_application, name='update_application'),
    path('application_delete/<int:id>/', views.application_delete, name='application_delete'),
    # Update Application if Status is pending(Parents)

    #path('download-admission-form/<int:id>/', views.download_admission_form, name='download_admission_form'),

    # School Side
    path('recieved_applications/', views.recieved_applications, name='recieved_applications')
    
]