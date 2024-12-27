from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart 
from school.models import School 
from django.http import JsonResponse 




# Create your views here.
def applications_summary(request):

    return render(request, 'applications_summary.html')

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

        response = JsonResponse({'school_name': school.schoolname})
        return response


def applications_delete(request):
    pass

    #return render(request, 'appication/applications_delete.html')


def applications_update(request):
    pass
    #return render(request, 'application/applications_update.html')