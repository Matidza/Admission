from django.db import models
import datetime


# Create your models here.

# Parents Model
class Parents(models.Model):
    
    username = models.CharField(max_length=100 )
    phone = models.CharField(max_length=10 )
    email = models.EmailField(max_length=100 )
    password = models.CharField(max_length=50 )
    image = models.ImageField(upload_to='uploads/parents/', default=datetime.datetime.today)

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name_plural = 'Parents'


# Schools Admin
class SchoolAdmin(models.Model):

    username = models.CharField(max_length=100 )
    phone = models.CharField(max_length=10 )
    email = models.EmailField(max_length=100 )
    password = models.CharField(max_length=50 )
    image = models.ImageField(upload_to='uploads/schooladmin/', default=datetime.datetime.today)

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name_plural = 'School Admin'


# Schools profile
class SchoolProfile(models.Model):

    schooladmin = models.ForeignKey(SchoolAdmin, on_delete=models.CASCADE)
    schoolname = models.CharField(max_length=100 )
    schooladdress = models.TextField(max_length=100, default="", blank=False) 
    address = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=100, default='', blank=True)
    website = models.TextField(max_length=100 ) 

    #curriculum
    #grade_levels
    #accreditationstatus


    #province = models.CharField(max_length=20, choices=('Limpopo', 'Gauteng', 'North West', 'Mpumalanga', 'Free State', 'KwaZulu Natal', 'Northern Cape', 'Western Cape', 'Eastern Cape'))
    #district
    
    #date = models.DateField(default=datetime.datetime.today)
    #image = models.ImageField(upload_to='uploads/schoolprofile/')
    def __str__(self):
        return self.schoolname
    
    class Meta:
        verbose_name_plural = 'School Profile'

class Admission(models.Model):
    def __str__(self):
        return self.admission



class ApplicationDecision(models.Model):
    Parents = models.ForeignKey(Parents, on_delete=models.CASCADE)
    SchoolProfile = models.ForeignKey(SchoolAdmin, on_delete=models.CASCADE)
    Admission = models.ForeignKey(Admission, on_delete=models.CASCADE)
    #status = models.CharField(max_length=20, choices=('Pending', 'Approved', 'Rejected'))

    def __str__(self):
        return self.status
