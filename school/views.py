from django.shortcuts import render, redirect, get_object_or_404
from .models import School , Sports, Academics
from .forms import SchoolInfo
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from django.contrib import messages
from admit.models import Profile


from django.db.models import Q 
from django.contrib.auth.models import User


@login_required(login_url='/login')
# Create your views here.
def schoolhomepage(request):
    school = School.objects.get(user=request.user)
    sports = Sports.objects.filter(school=school)
    academics = Academics.objects.filter(school=school)
    return render(request, "schoolhomepage.html", {'school': school, 'sports': sports, 'academics': academics})


def school_history(request):
    if request.user.is_authenticated:
        # Get the current user's school
        try:
            current_user = School.objects.get(id=request.user.id)
        except School.DoesNotExist:
            messages.error(request, "School profile not found!")
            return redirect('schoolhomepage')

        # Initialize the form with POST data and uploaded files
        form = SchoolInfo(request.POST or None, request.FILES or None, instance=current_user)

        if form.is_valid():
            form.save()
            messages.success(request, "Your information has been updated!")
            return redirect('schools:schoolhomepage')

        return render(request, "school_history.html", {'form': form})
    else:
        messages.error(request, "You must be logged in to access this page!")
        return redirect('schools:school_history')



@login_required(login_url='/login')
def sports(request):  
    current_user = School.objects.get(id=request.user.id)
    school = School.objects.get(user=request.user)
    sports = Sports.objects.filter(school=school)
    return render(request, 'sports.html', { 'sports': sports, 'current_user': current_user})



@login_required(login_url='login/')
def delete_sports(request, id):
    
    article = get_object_or_404(Sports, id=id)
    try:
        article.delete()
        messages.success(request, 'Article Deleted Successfully !')
        return redirect('schools:sports')
    except Exception as e:
        messages.error(request, 'Article Not Deleted')
        return redirect('schools:sports')


@login_required(login_url='/login')
def sportsform(request):
    if request.user.is_authenticated:
        current_user = School.objects.get(id=request.user.id)
        if request.method == 'POST':
            title = request.POST['title']
            image = request.FILES.get('image')
            date = request.POST['date']
            story = request.POST['story']

            article = Sports.objects.create(school=current_user, title=title, image=image, date=date, story=story)
            article.save()
            return redirect(reverse('schools:sports'))
        else:
            return render(request, 'sportsform.html', {'current_user': current_user})
    else:
        return redirect('home')
    


@login_required(login_url='/login')
def academics(request):
    current_user = School.objects.get(id=request.user.id)
    school = School.objects.get(user=request.user)
    academics = Academics.objects.filter(school=school)
    return render(request, 'academics.html', { 'academics': academics, 'current_user': current_user})


@login_required(login_url='login/')
def delete_academic(request, id):

    article = get_object_or_404(Academics, id=id)
    try:
        article.delete()
        messages.success(request, 'Article Deleted Successfully !')
        return redirect('schools:academics')
    except Exception as e:
        messages.error(request, 'Article Not Deleted')
        return redirect('schools:academics')


'''   
def searched(request):
    # check if user filed the form
    if request.method == 'POST':
        tittle = Academics.objects.all()
        story = Academics.objects.all()
        searched = request.POST['searched']
        searched = Academics.objects.filter(Q(title__icontains=searched) | Q(story__icontains=searched))

        user = User.objects.all()

        if not searched:
            messages.success(request, ("Searched Item Doesn't Not Exist"))
            return render(request, 'searches.html')
        else:
            return render(request, 'searches.html', {'user': user, 'searched': searched, 'tittle': tittle, 'story': story})
    else:
        return render(request, 'searches.html')
'''
@login_required(login_url='/login')
def  academicsform(request):
    if request.user.is_authenticated:
        current_user = School.objects.get(id=request.user.id)
        if request.method == 'POST':
       
            title = request.POST['title']
            image = request.FILES.get('image')  # Use FILES instead of File
            date = request.POST['date']
            story = request.POST['story']

            article = Academics.objects.create(school=current_user, title=title, image=image, date=date, story=story)
            article.save()
            return redirect(reverse('schools:academics'))  # Redirect to sports page after submission
        else:
            return render(request, 'academicsform.html', {'current_user': current_user})
    else:
        return redirect('home')



'''  
def schoolhomepage(request):
    school = School.objects.get(user=request.user)
    sports = Sports.objects.filter(school=school)
    paginator = Paginator(sports, 3)  # Show 3 sports per page
    page_number = request.GET.get('page')
    sports = paginator.get_page(page_number)
    return render(request, "schoolhomepage.html", {'school': school, 'sports': sports})
 '''

