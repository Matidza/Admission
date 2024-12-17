from django.shortcuts import render, redirect

# Create your views here.
def applications_summary(request):

    return render(request, 'applications_summary.html')


def applications_add(request):
    pass
    #return render(request, 'application/applications_add.html')


def applications_delete(request):
    pass

    #return render(request, 'appication/applications_delete.html')


def applications_update(request):
    pass
    #return render(request, 'application/applications_update.html')