from django.shortcuts import render
from .models import School , Sports, Academics
from django.core.paginator import Paginator


# Create your views here.
def schoolhomepage(request):
    school = School.objects.get(user=request.user)
    sports = Sports.objects.filter(school=school)
    return render(request, "schoolhomepage.html", {'school': school, 'sports': sports})


'''  
def schoolhomepage(request):
    school = School.objects.get(user=request.user)
    sports = Sports.objects.filter(school=school)
    paginator = Paginator(sports, 3)  # Show 3 sports per page
    page_number = request.GET.get('page')
    sports = paginator.get_page(page_number)
    return render(request, "schoolhomepage.html", {'school': school, 'sports': sports})
 '''

