from django.shortcuts import render, redirect
from .models import SchoolProfile
from django.contrib.auth import authenticate, login, logout

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


# Loging
def login_user(request):
    # Determine if user filled the form
    if request.method == 'POST':
        # Inputs linked to to the login.html form 
        # <input type="text" class="form-control" name="username" placeholder="Username"> 
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            
            #messages.success(request, ('Login Was Successful!'))
            return redirect('home')
        else:
            #messages.success(request, ('Login Not Successful! Try Again!!'))
            return redirect('login')
    else:
        return render(request, 'login.html', {})



# Logout
def logout_user(request):

    pass