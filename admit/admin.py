from django.contrib import admin
from .models import ParentProfile, SchoolProfile, AdmissionFormModel, ApplicationStatus
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(ParentProfile)

admin.site.register(SchoolProfile)
admin.site.register(AdmissionFormModel)
admin.site.register(ApplicationStatus)

