from django.contrib import admin
from .models import Parents, SchoolAdmin, Schoolprofile, AdmissionForm, ApplicationDecision
# Register your models here.
admin.site.register(Parents)
admin.site.register(SchoolAdmin)
admin.site.register(Schoolprofile)
admin.site.register(AdmissionForm)
admin.site.register(ApplicationDecision)