
from django.urls import path
from . import views

urlpatterns = [
    path('', views.applications_summary, name='applications_summary'),
    path('applyadmission/<int:school_id>/', views.applyadmission, name='applyadmission'),
    path('applications_add/', views.applications_add, name='applications_add'),
    path('applications_delete/', views.applications_delete, name='applications_delete'),
    path('applications_update/', views.applications_update, name='applications_update'),
    path('application/<int:id>/', views.application, name='application'),


    # School Side
    path('recieved_applications/', views.recieved_applications, name='recieved_applications')
    
]