from django.contrib import admin
from .models import Profile, SchoolProfile
from django.contrib.auth.models import User


# Register your models here.
admin.site.register(Profile)
admin.site.register(SchoolProfile)
#admin.site.register(AdmissionFormModel)
#admin.site.register(ApplicationStatus)


