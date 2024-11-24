from django.shortcuts import render

# Create your views here.
def schoolhomepage(request):
    return render(request, "schoolhomepage.html")