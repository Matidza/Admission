from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart 
from school.models import School 
from django.http import JsonResponse 
from django.contrib.auth.decorators import login_required

from .models import AdmissionForm
from django.contrib.auth.models import User
from django.contrib import messages

from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.



def applications_summary(request):
    applications = AdmissionForm.objects.filter(user=request.user)
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

def applications_delete(request):
    pass

    #return render(request, 'appication/applications_delete.html')


def applications_update(request):
    pass
    #return render(request, 'application/applications_update.html')




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
        grade = request.POST['grade']
        parentname = request.POST['parentname']
        
        status = request.POST['status']
        
        # Create a new AdmissionForm instance
        admissionform = AdmissionForm(
            user=current_user,
            school=school,
            childname=childname,
            childsurname=childsurname,
            grade=grade,
            parentname=parentname,
            
            status=status
        )
        
        # Save the admission form
        try:
            admissionform.save()
            messages.success(request, 'Application sent successfully!')
        except Exception as e:
            messages.error(request, 'Error sending application: ' + str(e))
        
        # Redirect the user
        return redirect('applications_summary')
    
    else:
        # Render the application form template
        return render(request, 'application_form.html', {'school': school})
    

# Schools recieved Applications
def recieved_applications(request):
    school = get_object_or_404(School, user=request.user)
    recieved_applications = AdmissionForm.objects.filter(school=school)
    return render(request, 'recieved_applications.html', {'recieved_applications': recieved_applications})


def application(request, id):
    applications = get_object_or_404(AdmissionForm, id=id)
    return render(request, 'parent_application.html', {'applications': applications})