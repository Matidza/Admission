from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User
from school.models import School


# Register your models here.
admin.site.register(Profile)

class ProfileInline(admin.StackedInline):
    model = Profile

class SchoolInline(admin.StackedInline):
    model = School
    extra = 0  # Prevent showing extra blank forms in the inline

    
# Extend the User model with Profile and School
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']  # Fields to display
    inlines = [ProfileInline, SchoolInline]  # Add both Profile and School inline

# Unregister the old User admin
admin.site.unregister(User)

# Register the new User admin
admin.site.register(User, UserAdmin)