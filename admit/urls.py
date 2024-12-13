
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('schools', views.schools, name='schools'),
    path('school/<int:pk>', views.school, name='school'),
    path('applications', views.applications, name='applications'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('filter,', views.filter, name='filter'),
]