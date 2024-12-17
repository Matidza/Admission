
from django.urls import path
from . import views

urlpatterns = [
    path('', views.applications_summary, name='applications_summary'),
    path('add/', views.applications_add, name='applications_add'),
    path('delete/', views.applications_delete, name='applications_delete'),
    path('update/', views.applications_update, name='applications_update'),
    
]