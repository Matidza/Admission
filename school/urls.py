from django.urls import path, include
from . import views


urlpatterns = [
    path('schoolhomepage/', views.schoolhomepage, name='schoolhomepage'),
    
]