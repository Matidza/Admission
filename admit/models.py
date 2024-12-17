from django.db import models
import datetime
from django.contrib.auth.models import User 
from django.db.models.signals import post_save


# Create your models here.

# Parents Model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(User, auto_now=True)
    phone = models.CharField(max_length=200, blank=True)
    address1 = models.CharField(max_length=200, blank=True)
    address2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    province = models.CharField(max_length=200, blank=True)
    zipcode = models.IntegerField( blank=True)
    country = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='uploads/parentprofile/')

    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name_plural = 'profile'
   



#class ApplicationStatus(models.Model):
    #admissionformmodel = models.ForeignKey(AdmissionFormModel, on_delete=models.CASCADE)
    #status = models.CharField(max_length=20, choices=('Pending', 'Approved', 'Rejected'))

 #   def __str__(self):
   #     return self.status
