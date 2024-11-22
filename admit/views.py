from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

# About page
def about(request):

    return render(request, 'about.html', {})

# All Schools page
def schools(request):
    return render(request, 'schools.html', {})


# All Schools page
def applications(request):
    return render(request, 'applications.html', {})