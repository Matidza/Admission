
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('schools', views.schools, name='schools'),
    path('applications', views.applications, name='applications'),
     path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]