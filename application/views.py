from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart 
from school.models import School 
from django.http import JsonResponse 
from django.contrib.auth.decorators import login_required

from .models import AdmissionForm, Status
from django.contrib.auth.models import User
from django.contrib import messages
from admit.models import Profile

from django.shortcuts import get_object_or_404, redirect, render

from django.core.mail import send_mail
from django.urls import reverse

# Create your views here.



def applications_summary(request):
    applications = AdmissionForm.objects.filter(user=request.user).select_related('status')
    return render(request, 'applications_summary.html', {'applications': applications})

'''  
def applications_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        school_id = int(request.POST.get('school_id'))

        school = get_object_or_404(School, id=school_id)

        cart.add(school=school)

        resonse = JsonResponse({'School Name: ': school.schoolname})
        return resonse
    #return render(request, 'application/applications_add.html')'''

'''   
Add 
'''
'''  
'''
def applications_add(request):
    if request.POST.get('action') == 'post':
        # Retrieve the cart
        cart = Cart(request)
        # get school stuff like its id
        school_id = int(request.POST.get('school_id'))
        # Look up school in the school database
        school = get_object_or_404(School, id=school_id)

        # Add the school and its stuff(id, schoolname, schoolemail etc) to the cart
        cart.add(school=school)

        response = JsonResponse({'school_name': school.schoolname, 'school_id': school.id})
        print(response)
        return response

def application_delete(request, id):
    application = get_object_or_404(AdmissionForm, id=id)

    try:
        application.delete()
        messages.success(request, 'Application withdrawn!')
        return redirect('application:applications_summary')
    except Exception as e:
        messages.error(request, 'Application not withdrawn!')
        return redirect('application:applications_summary')

    #return render(request, 'appication/applications_delete.html')

# Update Application if Status is pending(Parents)
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import AdmissionForm

@login_required(login_url='/login')
def update_application(request, id):
    # Safely fetch the application form or redirect if not found
    application_form = get_object_or_404(AdmissionForm, id=id)

    if request.method == 'POST':
        # Update only fields that are allowed
        childname = request.POST.get('childname')
        if childname:
            application_form.childname = childname
            application_form.save()
            return redirect('application:applications_summary')
        else:
            return render(request, 'update_application.html', {
                'application_form': application_form,
                'error': 'Child name cannot be empty.'
            })
    
    # For GET request, show the form with existing data
    return render(request, 'update_application.html', {'application_form': application_form})


@login_required(login_url='/login')
def applyadmission(request, school_id):
    # Get the current logged-in user
    current_user = request.user
    
    # Look up the school in the database
    school = get_object_or_404(School, id=school_id)
    
    if request.method == 'POST':
        # Get the form data
        childname = request.POST['childname']
        childsurname = request.POST['childsurname']
        id_number = request.POST['id_number']
        grade = request.POST['grade']
        parentname = request.POST['parentname']
        
        #statuss = request.POST['statuss']
        
        # Create a new AdmissionForm instance
        admissionform = AdmissionForm(
            user=current_user,
            school=school,
            childname=childname,
            childsurname=childsurname,
            grade=grade,
            parentname=parentname,
            
            #statuss=statuss,
           
        )
        # check if childs names with Id number has already applied to this school 
        # Save the admission form
        try:
            admissionform.save()

            # send Email to School and Parent/Gurdian to confirm submitted application
            user_email = current_user.email
            subject = f'Application to SchoolName'
            message = f"Your application  for {childname} was sent to {school}. {school} will keep in touch with you with regards to your application. Or you can always check your application status on views.com"
            print(f"Your application to {school} for {childname} was sent. {school} will keep in touch with you with regards to your application. Or you can always check your application status on views.com")          
            
            send_mail(
                subject = subject,
                message = message,
                from_email = "admissions.django@gmail.com",
                recipient_list = [user_email],
                fail_silently = False,
            )

            messages.success(request, 'Application sent successfully!')
        except Exception as e:
            messages.error(request, 'Error sending application: ' + str(e))      
        # Redirect the user
        return redirect('application:applications_summary')
    else:
        # Render the application form template
        return render(request, 'application_form.html', {'school': school})
    

# Schools recieved Applications
def recieved_applications(request):
    school = get_object_or_404(School, user=request.user)  
    recieved_applications = AdmissionForm.objects.filter(school=school).select_related('status')  
    return render(request, 'recieved_applications.html', {'recieved_applications': recieved_applications})


def application(request, id):
    # Get the admission form based on the id
    application_form = get_object_or_404(AdmissionForm, id=id) 
    # Retrieve the status associated with this admission form
    status = application_form.status  # This uses the related_name 'status' in the Status model  
    # Pass the application form and its status to the template
    return render(request, 'parent_application.html', {
        'application': application_form,
        'status': status
    })


from django.utils.http import url_has_allowed_host_and_scheme
from django.conf import settings
from django.core.exceptions import ValidationError
from django.contrib import messages


from django.core.exceptions import ValidationError
from django.contrib import messages
from django.utils.http import url_has_allowed_host_and_scheme
@login_required(login_url='/login')
def update_application_status(request, id):
    application_form = get_object_or_404(AdmissionForm, id=id)
    status = get_object_or_404(Status, admissionform=application_form)

    if request.method == 'POST':
        new_status = request.POST.get('degree')
        reason = request.POST.get('reason', '').strip()

        if new_status in ['Pending', 'Wait-listed', 'Rejected'] and not reason:
            messages.error(request, 'Reason is required for the selected status.')
            return redirect(request.path_info)

        status.status = new_status
        status.reason = reason

        try:
            status.save()
            messages.success(request, 'Status updated successfully.')
            next_url = request.GET.get('next')
            if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
                return redirect(next_url)
            return redirect('application:recieved_applications')
        except ValidationError as e:
            for error in e.messages:
                messages.error(request, error)

    return render(request, 'status.html', {
        'status': status,
        'application_form': application_form
    })




