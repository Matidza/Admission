from django.contrib import admin
from .models import School ,  Sports , Academics
# Register your models here.

admin.site.register(School)
admin.site.register(Academics)
admin.site.register(Sports)