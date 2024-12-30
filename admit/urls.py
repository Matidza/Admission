
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('schools', views.schools, name='schools'),
    path('school/<int:pk>', views.school, name='school'),
    path('admission', views.admission, name='admission'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('filters/<str:fil>/', views.filters, name='filters'),
    path('search/', views.search, name='search'),

    path('update_user/', views.update_user, name='update_user'),
    path('update_password/', views.update_password, name='update_password'),
    path('update_info/', views.update_info, name='update_info'),
]