from django.shortcuts import render
from .models import SchoolProfile

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

# About page
def about(request):

    return render(request, 'about.html', {})

# All Schools page
def schools(request):
    school_profile = SchoolProfile.objects.all()
    return render(request, 'schools.html', {'school_profile': school_profile})


# All Schools page
def applications(request):
    return render(request, 'applications.html', {})