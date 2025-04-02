from django.contrib import admin
from .models import AdmissionForm, Status

# Register your models here.
admin.site.register(AdmissionForm)
admin.site.register(Status)