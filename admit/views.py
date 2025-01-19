from django.shortcuts import render, redirect
from school.models import School, Sports
from .models import Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.contrib.auth.models import User
from .forms import SignUpForm
from django.db.models import Q
from django.urls import reverse
from .forms import UpdateUserForm, ChangePasswordForm, UserInfoForm

from school.forms import SchoolInfo
from django.shortcuts import redirect
from django.contrib import messages 


# Create your views here.
def home(request):
    return render(request, 'parent/home.html', {})

# About page


def about(request):

    return render(request, 'parent/about.html', {})

# All Schools page



def schools(request):
    school_profile = School.objects.all()
    #province = Province.objects.all()
    return render(request, 'parent/schools.html', {'school_profile': school_profile})#, 'province': province

# Individual School {page}


def school(request, pk):
    # Get the School Id form the SchoolAddress model
    school = School.objects.get(id=pk)
    sports = Sports.objects.filter(school=school)
    return render(request, 'parent/school.html', {'school': school, 'sports':sports} ) # using template from parent app
    #return render(request, 'schoolhomepage.html', {'school': school})

'''
def school(request, pk):
    # Get the School Id form the SchoolAddress model
    school = School.objects.get(id=pk)
    sports = Sports.objects.filter(school=school)
    #return render(request, 'parent/school.html', {'school': school}) # using template from parent app
    return render(request, 'schoolhomepage.html', {'school': school , 'sports':sports})

    
def school(request, pk):
    current_user = Profile.objects.get(user__id=request.user.id)
    if not request.user.is_authenticated:
        # Handle unauthenticated users
        return HttpResponseForbidden("Access denied")

    school = School.objects.get(id=pk)
    sports = Sports.objects.filter(school=school)
    
    if current_user.user_type == 'parent':
        return render(request, 'parent/school.html', {'school': school, 'sports': sports})
    elif current_user.user_type == 'school':
        return render(request, 'schoolhomepage.html', {'school': school, 'sports': sports})
'''



''''
Lets filter the schools by province, district, circuit
'''
def filters(request, fil):
    # Convert the filter string from URL (replace hyphens with spaces)
    """
    Filter schools based on the provided province name from the URL.

    Args:
        request: The HTTP request object.
        fil (str): The filter string representing the province name, 
                   with hyphens replacing spaces.

    Returns:
        HttpResponse: Renders the 'parent/schools.html' template with the filtered 
                      schools and province if the province is found.
        HttpResponseRedirect: Redirects to the home page with an error message 
                              if the province does not exist.

    """

    fil = fil.replace('-', ' ')
    try:
        # Fetch the province using the name
        province = School.objects.get(provinc=fil)

        # Filter schools that belong to the selected province
        schools = School.objects.filter(province=province)

        # Pass the filtered schools and province to the template
        return render(request, 'parent/schools.html', {'province': province, 'school_profile': schools})
    except School.DoesNotExist:
        # Show an error message if the province is not found
        messages.error(request, "Filter doesn't exist!")
        return redirect('home')


@login_required(login_url='/login')
# All Schools page
def admission(request):
    return render(request, 'parent/admission.html', {})


# Loging
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect, render

def login_user(request):
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

            # Redirect based on user type
            if user.profile.user_type == 'school':
                return redirect(reverse('schools:schoolhomepage'))  # Replace 'applications' with the actual URL name for the applications page
            elif user.profile.user_type == 'parent':
                return redirect('home')  # Redirect parents to the home page
            else:
                return redirect('home')  # Default redirect for other user types
        else:
            # Authentication failed, display error message
            messages.success(request, 'Login details invalid! Try Again!!')
            return redirect('login')
    else:
        # Render the login form for GET requests
        return render(request, 'parent/login.html', {})

'''
def login_user(request):
   
    Handle user login.

    If the request method is POST, authenticate the user and log them in. 
    If authentication is successful, redirect to the home page. 
    Otherwise, display an error message and redirect to the login page.
    If the request method is not POST, render the login form.
   
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
'''

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
            messages.success(
                request, ('Username & Account Created, Fill Out User Info. '))
            return redirect('update_info')
        else:
            messages.success(
                request, ('Registration Not Successfully. Try Again!!'))
            return redirect('register')
    else:
        return render(request, 'parent/register.html', {'form': form})


# search
def search(request):
    # check if user filed the form
    if request.method == 'POST':
        province = School.objects.all()
        school_profile = School.objects.all()
        searched = request.POST['searched']
        searched = School.objects.filter(Q(schoolname__icontains=searched))
        user = User.objects.all()

        if not searched:
            messages.success(request, ("Searched Item Doesn't Not Exist"))
            return render(request, 'parent/search.html')
        else:
            return render(request, 'parent/search.html', {'user': user, 'searched': searched, 'school_profile': school_profile, 'province': province})
    else:
        return render(request, 'parent/search.html')


# Update user Login details
@login_required(login_url='/login')
def update_user(request):
	if request.user.is_authenticated:
        # What/Which user is authenticated/
		current_user = User.objects.get(id=request.user.id)
        # create form
		user_form = UpdateUserForm(request.POST or None, instance=current_user)

        # Validate  the form and its content and login user
		if user_form.is_valid():
			user_form.save()
			login(request, current_user)
			messages.success(request, "User Has Been Updated!!")
			return redirect('logout')
		return render(request, "parent/update_user.html", {'user_form':user_form})
	else:
		messages.success(request, "You Must Be Logged In To Access That Page!!")
		return redirect('home')
     


@login_required(login_url='/login')
def update_password(request):
    # Authenticate User
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == 'POST':
            form = ChangePasswordForm(current_user, request.POST)

            if form.is_valid():
                form.save()
                messages.success(request, "Password Updated!!")
                login(request, current_user)
                return redirect('logout')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                    return redirect('update_password')
        else:
            form = ChangePasswordForm(current_user)
            return render(request, "parent/update_password.html", {'form':form})#          
    else:
        messages.success(request, "You Must Be Logged In To Access That Page!!")
        return redirect('home')
    




def update_info(request):
    if request.user.is_authenticated:
        # Get Current User Profile
        current_user = Profile.objects.get(user__id=request.user.id)

        # Get original User Form
        form = UserInfoForm(request.POST or None, instance=current_user)

        if form.is_valid():
            form.save()# Save the form

            # Check the user type and redirect accordingly
            if current_user.user_type == "school":
                messages.success(request, "Your Info Has Been Updated!!")
                return redirect('update_school_info')
            
            elif current_user.user_type == "parent":
                messages.success(request, "Your Info Has Been Updated!!")
                return redirect('logout')

        return render(request, "parent/update_info.html", {'form': form})
    else:
        messages.error(request, "You Must Be Logged In To Access That Page!!")
        return redirect('login')



def update_school_info(request):
    if request.user.is_authenticated:
        # Get the current user's school
        try:
            current_user = School.objects.get(user__id=request.user.id)
        except School.DoesNotExist:
            messages.error(request, "School profile not found!")
            return redirect('logout')

        # Initialize the form with POST data and uploaded files
        form = SchoolInfo(request.POST or None, request.FILES or None, instance=current_user)

        if form.is_valid():
            form.save()
            messages.success(request, "Your information has been updated!")
            return redirect('logout')

        return render(request, "parent/update_school_info.html", {'form': form})
    else:
        messages.error(request, "You must be logged in to access this page!")
        return redirect('home')
     

'''   
def update_school_info(request):
    if request.user.is_authenticated:
        try:
            # Get Current User's School Info
            current_user = School.objects.get(user__id=request.user.id)
        except School.DoesNotExist:
            # If no School info exists for the user, handle it gracefully
            messages.error(request, "No School info found for this user.")
            return redirect('home')

        # Get the form for updating School info, including file data
        if request.method == 'POST' and request.FILES:
            form = SchoolInfo(request.POST, request.FILES, instance=current_user)
        else:
            form = SchoolInfo(instance=current_user)

        if form.is_valid():
            # Save the form if it's valid
            form.save()
            messages.success(request, "Your info has been updated!")
            return redirect('logout')  # or another redirect destination like a dashboard

        return render(request, "parent/update_school_info.html", {'form': form})

    else:
        # If the user is not authenticated
        messages.error(request, "You must be logged in to access that page.")
        return redirect('login')  ''' # Redirect to login page