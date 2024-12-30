from django.shortcuts import render
from .models import School  

# Create your views here.
def schoolhomepage(request):

    school = School.objects.get(user=request.user) 
    return render(request, "schoolhomepage.html", {'school': school})


