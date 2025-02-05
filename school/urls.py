from django.urls import path, include
from . import views

app_name = 'schools' 
urlpatterns = [
    path('schoolhomepage/', views.schoolhomepage, name='schoolhomepage'),

    path('sports/', views.sports, name='sports'),
    path('sportsform/', views.sportsform, name='sportsform'),  
    path('delete/<int:id>/', views.delete_sports, name='delete_sports'),

    path('academics/', views.academics, name='academics'),
    path('academicsform/', views.academicsform, name='academicsform'),
    path('delete/<int:id>/', views.delete_academic, name='delete_academic'),
    #path('search/', views.searched, name='searched'),

    path('school_history/', views.school_history, name='school_history'),

    
]