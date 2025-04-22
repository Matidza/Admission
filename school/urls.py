from django.urls import path, include
from . import views

app_name = 'schools' 
urlpatterns = [
    path('schoolhomepage/', views.schoolhomepage, name='schoolhomepage'),
    path('sport_article/<int:id>', views.sport_article, name='sport_article'),

    path('sports/', views.sports, name='sports'),
    path('sportsform/', views.sportsform, name='sportsform'),  
    path('delete/<int:id>/', views.delete_sports, name='delete_sports'),
    path('update_sports_article/<int:id>', views.update_sports_article, name='update_sports_article'),
    

    path('academics/', views.academics, name='academics'),
    path('academic_article/<int:id>', views.academic_article, name='academic_article'),
    path('academicsform/', views.academicsform, name='academicsform'),
    path('delete_academic/<int:id>/', views.delete_academic, name='delete_academic'),
    path('update_academic_article/<int:id>', views.update_academic_article, name='update_academic_article'),
    #path('search/', views.searched, name='searched'),
    
 
]