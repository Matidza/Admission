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


# Create your views here.
@login_required(login_url='/login')
def schoolhomepage(request):
    
    school = get_object_or_404(School, user=request.user)
    sports = Sports.objects.filter(school=school).order_by('-date_modified')
    academics = Academics.objects.filter(school=school).order_by('-date_modified')
    return render(request, "schoolhomepage.html", {'school': school, 'sports': sports, 'academics': academics})

def sport_article(request, id):
    sport_article = get_object_or_404(Sports, id=id)
    return render(request, 'sports_id.html', {'sport_article': sport_article})
    



@login_required(login_url='/login')
def sports(request):  
    # Retrieve the School object associated with the logged-in user
    school = get_object_or_404(School, user=request.user)
    
    # Query all sports records for the retrieved school
    sports = Sports.objects.filter(school=school).order_by('-date_modified')
    
    return render(request, 'sports.html', { 'sports': sports, 'current_user': school })



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
def update_sports_article(request, id):
    current_user = get_object_or_404(School, user=request.user) 
    try:
        sport_article = Sports.objects.get(id=id)
    except Sports.DoesNotExist:
        return redirect('home')

    if request.method == 'POST':
        sport_article.title = request.POST['title']
        sport_article.image = request.FILES.get('image')
        sport_article.date = request.POST['date']
        sport_article.story = request.POST['story']
        sport_article.save()
        return redirect('schools:sports')
    else:
        return render(request, 'update_sports.html', {'sport_article': sport_article, 'current_user': current_user})





@login_required(login_url='/login')
def sportsform(request):
    # Use get_object_or_404 for better error handling
    current_user = get_object_or_404(School, user=request.user)

    if request.method == 'POST':
        title = request.POST['title']
        image = request.FILES.get('image')
        date = request.POST['date']
        story = request.POST['story']

        # Create a new Sports article
        article = Sports.objects.create(
            school=current_user,
            title=title,
            image=image,
            date=date,
            story=story
        )
        article.save()

        # Redirect to the sports page
        return redirect(reverse('schools:sports'))
    else:
        return render(request, 'sportsform.html', {'current_user': current_user})
    











@login_required(login_url='/login')
def academics(request):
    # Ensure the school object is retrieved using the user relationship
    school = get_object_or_404(School, user=request.user)
    
    # Query all academic articles associated with the school
    academics = Academics.objects.filter(school=school).order_by('-date_modified')
    return render(request, 'academics.html', { 'academics': academics, 'current_user': school })


def academic_article(request, id):
    academic_article = get_object_or_404(Academics, id=id)
    return render(request, 'academic_id.html', {'academic_article': academic_article})


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

@login_required(login_url='/login')
def update_academic_article(request, id):
    current_user = get_object_or_404(School, user=request.user)
    try:
        academic_article = Academics.objects.get(id=id)
    except Academics.DoesNotExist:
        return redirect('home')
    if request.method == 'POST':
        academic_article.title = request.POST['title']
        academic_article.image = request.FILES.get('image')
        academic_article.date = request.POST['date']
        academic_article.story = request.POST['story']
        academic_article.save()
        return redirect('schools:academics')  # Change this to the correct URL name
    else:
        return render(request, 'update_academics_article.html', {'academic_article': academic_article, 'current_user': current_user})

@login_required(login_url='/login')
def academicsform(request):
    # Get the School object associated with the logged-in user
    current_user = get_object_or_404(School, user=request.user)

    if request.method == 'POST':
        title = request.POST['title']
        image = request.FILES.get('image')  # Use FILES to handle file uploads
        date = request.POST['date']
        story = request.POST['story']

        # Create the new academic article
        article = Academics.objects.create(
            school=current_user,
            title=title,
            image=image,
            date=date,
            story=story
        )
        article.save()

        # Redirect to the academics page
        return redirect(reverse('schools:academics'))
    else:
        return render(request, 'academicsform.html', {'current_user': current_user})



'''    
def schoolhomepage(request):
    school = School.objects.get(user=request.user)
    sports = Sports.objects.filter(school=school)
    paginator = Paginator(sports, 3)  # Show 3 sports per page
    page_number = request.GET.get('page')
    sports = paginator.get_page(page_number)
    return render(request, "schoolhomepage.html", {'school': school, 'sports': sports})
 '''
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
