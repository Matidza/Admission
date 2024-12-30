from django.urls import path, include
from . import views

app_name = 'schools' 
urlpatterns = [
    path('schoolhomepage/', views.schoolhomepage, name='schoolhomepage'),
    
]