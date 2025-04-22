
from django.urls import path
from . import views

#app_name = 'admit' 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('schools/', views.schools, name='schools'),
    path('school/<int:pk>', views.school, name='school'),
    path('sport_art/<int:id>', views.sport_art, name='sport_art'),
    path('academic_art/<int:id>', views.academic_art, name='academic_art'),
    path('schools/<int:id>/academic-articles/', views.all_academic_articles, name='all_academic_articles'),
    path('schools/<int:id>/sports-articles/', views.all_sports_articles, name='all_sports_articles'),
    path('schools/<int:id>/contact/', views.contact, name='contact'),



    
    path('admission/', views.admission, name='admission'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('filters/<str:fil>/', views.filters, name='filters'),
    path('district/<str:fil>/', views.district, name='district'),
    path('search/', views.search, name='search'),

    path('update_user/', views.update_user, name='update_user'),
    path('update_password/', views.update_password, name='update_password'),
    path('update_info/', views.update_info, name='update_info'),

    path('update_school_info/', views.update_school_info, name='update_school_info'),
    #path('view_sports/', views.view_sports, name='view_sports'),
]