from django.shortcuts import render, redirect
from .models import SchoolProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import SignUpForm



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
    # Determine if user has filled the form, if not request the for to fil it
    if request.method == 'POST':

        # Inputs linked to to the login.html form 
        # <input type="text" class="form-control" name="username" placeholder="Username"> 
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        # Loging the authenticated user
        if user is not None:
            login(request, user)
            #messages.success(request, ('Login Was Successful!'))
            return redirect('home')
        # Redirect the user if login detsails arev not authenticated
        else:
            messages.success(request, ('Login Not Successful! Try Again!!'))
            return redirect('login')
        #  Render all the above function on the html file
    else:
        return render(request, 'login.html', {})



# Logout
def logout_user(request):
    logout(request)
    messages.success(request, ("Logged Out!"))
    return redirect('home')

def register_user(request):
    
    form = SignUpForm()

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('Username & Account Created, Fill Out User Info. '))
            return redirect('home') 
        else:
            messages.success(request, ('Registration Not Successfully. Try Again!!'))
            return redirect('register')   
    else:
        return render(request, 'register.html', {'form':form})