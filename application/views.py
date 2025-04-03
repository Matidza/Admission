from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart 
from school.models import School 
from django.http import JsonResponse 
from django.contrib.auth.decorators import login_required

from .models import AdmissionForm, Status
from django.contrib.auth.models import User
from django.contrib import messages

from django.shortcuts import get_object_or_404, redirect, render

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
            id_number=id_number,
        )
        # check if childs names with Id number has already applied to this school 
        # Save the admission form
        try:
            admissionform.save()
            # send Email to School and Parent/Gurdian to confirm submitted application
            # send_mail()
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

@login_required(login_url='/login')
def update_application_status(request, id):
    try:
        application_form = get_object_or_404(AdmissionForm, id=id)
    except AdmissionForm.DoesNotExist:
        return redirect('application')

    if request.method == 'POST':
        application_form.status = request.POST['status']
        application_form.save()
        return redirect('application')
    else:
        return render(request, 'status.html', {'application': application_form})





from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import AdmissionForm  # Ensure you import your models

def download_admission_form(request, id):
    # Get the application data
    application = get_object_or_404(AdmissionForm, id=id)

    # Create the response object with a PDF content type
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="Admission_Form_{application.childname}.pdf"'

    # Create a PDF document
    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter

    # Set Title
    p.setFont("Helvetica-Bold", 16)
    p.drawString(200, height - 50, f"Admission Form for {application.childname}")

    # Set Application Details
    p.setFont("Helvetica", 12)
    p.drawString(100, height - 100, f"Application No: {application.id}")
    p.drawString(100, height - 120, f"School: {application.school.schoolname}")
    p.drawString(100, height - 140, f"Grade Applied: {application.grade}")
    p.drawString(100, height - 160, f"Admission Year: 2026")
    p.drawString(100, height - 180, f"Date Applied: {application.date_applied}")
    p.drawString(100, height - 200, f"Status: {application.status}")

    # Child's Information
    p.setFont("Helvetica-Bold", 14)
    p.drawString(100, height - 240, "Child's Information")

    p.setFont("Helvetica", 12)
    p.drawString(100, height - 260, f"Name: {application.childname}")
    p.drawString(100, height - 280, f"Surname: {application.childsurname}")
    p.drawString(100, height - 300, f"Gender: {application.child.gender}")  # Adjusted here
    p.drawString(100, height - 320, f"Nationality: {application.nationality}")
    p.drawString(100, height - 340, f"ID/Passport No: {application.id_or_passport}")

    # Save the PDF document
    p.showPage()
    p.save()

    return response
