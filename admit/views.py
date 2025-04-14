from django.shortcuts import render, redirect, get_object_or_404
from school.models import School, Sports, Academics
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

from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect, render


from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def home(request):
    return render(request, 'parent/home.html', {})

# About page
def about(request):
    return render(request, 'parent/about.html', {})




# School Details
from django.core.paginator import Paginator

def schools(request):
    school_profile = School.objects.all()
    paginator = Paginator(school_profile, 6)  # 5 schools per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'parent/schools.html', {'page_obj': page_obj})



# Individual School {page}
def school(request, pk):
    school = School.objects.get(id=pk)
    sports = Sports.objects.filter(school=school).order_by('-date_modified')
    academics = Academics.objects.filter(school=school).order_by('-date_modified')
    return render(request, 'parent/school.html', {'school': school, 'sports': sports, 'academics': academics})



def sport_art(request, id): 
    sport_art = get_object_or_404(Sports, id=id)
    return render(request, 'sports_d.html', {'sport_art': sport_art})

def academic_art(request, id): 
    academic_art = get_object_or_404(Academics, id=id)
    return render(request, 'academic_art.html', {'academic_art': academic_art})


# All Academic Articles
def all_academic_articles(request, id):
    school = get_object_or_404(School, id=id)
    academics = Academics.objects.filter(school=school).order_by('-date_modified')
    return render(request, 'all_academic_articles.html', {
        'academics': academics,
        'school': school
    })

# All Sports Articles
def all_sports_articles(request, id):
    school = get_object_or_404(School, id=id)
    sports = Sports.objects.filter(school=school).order_by('-date_modified')
    return render(request, 'all_sports_articles.html', {
        'sports': sports,
        'school': school
    })


# contact info
def contact(request, id):
    school = get_object_or_404(School, id=id)

    return render(request, 'parent/contact.html', {'school': school})

def email(request,id):
    school = get_object_or_404(School, id=id)

    if request.method == 'POST':
        
        #fullname = request.POST.get('fullname', '').strip()
        subject = request.POST.get('subject', '').strip()
        email = request.POST.get('email', '').strip().lower()
        message = request.POST.get('message', '').strip()
        print(f'Subject: {subject} \n from: {email} \n message: {message} ')
        # Send email to the school
        send_mail(
            subject=subject,
            message=message,
            from_email=email,
            recipient_list=[school.schoolemail],
            fail_silently=False,
        )

        # Return a success message or redirect to a thank-you page
        return render(request, 'parent/contact.html', {'school': school})
    else:
        return render(request, 'parent/contact.html', {'school': school})

'''  
def view_sports(request):
    #current_user = School.objects.get(id=request.user.id)
    sports = Sports.objects.filter(school=school)
    academics = Academics.objects.filter(school=school)
    return render(request, 'parent/view_sports.html', {'sports': sports, 'school':school})'''

# Update Schools Academics
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

# Filter Schools by Province
def filters(request, fil):
    fil = fil.replace('-', ' ')  # Convert URL-friendly text back to normal
    school_profile = School.objects.filter(provinc=fil)
    paginator = Paginator(school_profile, 10)  # 5 schools per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'parent/filter.html', {'page_obj': page_obj, 'selected_province': fil})




def district(request, fil):
    fil = fil.replace('-', ' ')  # Convert URL-friendly text back to normal
    school_profile = School.objects.filter(district=fil)
    return render(request, 'parent/filter.html', {'school_profile': school_profile, 'selected_province': fil})




@login_required(login_url='/login')
# All Schools page
def admission(request):
    return render(request, 'parent/admission.html', {})


# Login User
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

# Logout User
def logout_user(request):
    logout(request)
    messages.success(request, ("Logged Out!"))
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



# Search School
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




# Update User Login details
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
     


# Register User
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from .forms import SignUpForm

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']

            user = authenticate(username=username, password=password)
            login(request, user)

            # Send confirmation email
            send_mail(
                'Welcome to [Your Website Name]',
                'Hi {}, thank you for registering at [Your Website Name].'.format(username),
                'your_email@example.com',  # Replace with your sender email address
                [email],
                fail_silently=False,
            )

            messages.success(request, 'Username & Account Created. A confirmation email has been sent.')
            return redirect('update_info')
        else:
            messages.error(request, 'Registration Not Successful. Try Again!')
            return redirect('register')
    else:
        return render(request, 'parent/register.html', {'form': form})




# Update Profile
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



# Update School Info
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

