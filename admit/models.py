from django.db import models
import datetime


# Create your models here.

# Parents Model
class ParentProfile(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    #date_modified = models.DateTimeField(User, auto_now=True)
    phone = models.CharField(max_length=200, blank=True)
    address1 = models.CharField(max_length=200, blank=True)
    address2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    province = models.CharField(max_length=200, blank=True)
    zipcode = models.IntegerField( blank=True)
    country = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='uploads/parentprofile/')

    def __str__(self):
        return self.phone
    class Meta:
        verbose_name_plural = 'Parent Profile'

class SchoolProfile(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    #date_modified = models.DateTimeField(User, auto_now=True)
    schoolname = models.CharField(max_length=100 )
    schooladdress = models.TextField(max_length=100, default="", blank=False)
    telephone = models.CharField(max_length=200, blank=True)
    address1 = models.CharField(max_length=200, blank=True)
    address2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    province = models.CharField(max_length=200, blank=True)
    zipcode = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)
    website = models.TextField(max_length=100 ) 
    image = models.ImageField(upload_to='uploads/schoolprofile/', default=datetime.datetime.today)
    #curriculum
    #grade_levels
    #accreditationstatus
    #province = models.CharField(max_length=20, choices=('Limpopo', 'Gauteng', 'North West', 'Mpumalanga', 'Free State', 'KwaZulu Natal', 'Northern Cape', 'Western Cape', 'Eastern Cape'))
    #district
    #date = models.DateField(default=datetime.datetime.today)

    def __str__(self):
        return self.schoolname
    class Meta:
        verbose_name_plural = 'School Profile'




class AdmissionFormModel(models.Model):
    parentprofile = models.ForeignKey(ParentProfile, on_delete=models.CASCADE)
    childname = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.childname



class ApplicationStatus(models.Model):
    admissionformmodel = models.ForeignKey(AdmissionFormModel, on_delete=models.CASCADE)
    #status = models.CharField(max_length=20, choices=('Pending', 'Approved', 'Rejected'))

    def __str__(self):
        return self.status
