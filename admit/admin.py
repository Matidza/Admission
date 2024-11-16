from django.contrib import admin
from .models import Parents, SchoolAdmin, SchoolProfile, Admission, ApplicationDecision
# Register your models here.
admin.site.register(Parents)
admin.site.register(SchoolAdmin)
admin.site.register(SchoolProfile)
admin.site.register(Admission)
admin.site.register(ApplicationDecision)