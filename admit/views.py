from django.shortcuts import render, redirect
from school.models import School, Province

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.contrib.auth.models import User
from .forms import SignUpForm



# Create your views here.
def home(request):
    return render(request, 'parent/home.html', {})

# About page
def about(request):

    return render(request, 'parent/about.html', {})

# All Schools page
def schools(request):
    school_profile = School.objects.all()
    return render(request, 'parent/schools.html', {'school_profile': school_profile})

# Individual School {page}
def school(request, pk):
    # Get the School Id form the SchoolAddress model
    school = School.objects.get(id=pk)
    return render(request, 'parent/school.html', {'school':school})



''''
Lets filter the schools by province, district, circuit
'''
def filters(request, fil):
    fil = fil.replace('-', ' ')
    # Filter the province Model
    try:
        province = Province.objects.get(name=fil)
        schools = School.objects.filter(province=province)
        return render(request, 'parent/filter.html', {'province':province, 'schools':schools})

    except:
        messages.success(request, ("Filter Doesn't Exist!"))
        return redirect('home')



@login_required(login_url='/login')
# All Schools page
def applications(request):
    return render(request, 'applications.html', {})


# Loging
def login_user(request):
    """
    Handle user login.

    If the request method is POST, authenticate the user and log them in. 
    If authentication is successful, redirect to the home page. 
    Otherwise, display an error message and redirect to the login page.
    If the request method is not POST, render the login form.
    """
    if request.method == 'POST':
        # Retrieve username and password from the request
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Log in the authenticated user
            login(request, user)
            messages.success(request, 'Login Was Successful!')
            return redirect('home')
        else:
            # Authentication failed, display error message
            messages.error(request, 'Login Not Successful! Try Again!!')
            return redirect('login')
    else:
        # Render the login form for GET requests
        return render(request, 'parent/login.html', {})



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
            return redirect('login') 
        else:
            messages.success(request, ('Registration Not Successfully. Try Again!!'))
            return redirect('register')   
    else:
        return render(request, 'parent/register.html', {'form':form})