from django.db import models
import datetime
# Create your models here.

class Parents(models.Model):
    
    name = models.CharField(max_length=100 )
    surname = models.CharField(max_length=100 ) 
    phone = models.CharField(max_length=10 )
    email = models.EmailField(max_length=100 )
    password = models.CharField(max_length=50 )
    image = models.ImageField(upload_to='uploads/product/')

    def __str__(self):
        return self.namne
    
    class Meta:
        verbose_name_plural = 'Parents'

class SchoolAdmin(models.Model):

    name = models.CharField(max_length=100 )
    phone = models.CharField(max_length=10 )
    email = models.EmailField(max_length=100 )
    password = models.CharField(max_length=50 )

    def __str__(self):
        return self.namne
    
class Schoolprofile(models.Model):

    school = models.ForeignKey(SchoolAdmin, on_delete=models.CASCADE)
    name = models.CharField(max_length=100 )
    address = models.TextField(max_length=100 ) 
    address = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=100, default='', blank=True)
    website = models.TextField(max_length=100 ) 

    #curriculum
    #grade_levels
    #accreditationstatus


    #province = models.CharField(max_length=20, choices=('Limpopo', 'Gauteng', 'North West', 'Mpumalanga', 'Free State', 'KwaZulu Natal', 'Northern Cape', 'Western Cape', 'Eastern Cape'))
    #district
    
    date = models.DateField(default=datetime.datetime.today)
    image = models.ImageField(upload_to='uploads/product/')
    def __str__(self):
        return self.namne

class AdmissionForm(models.Model):
    def __str__(self):
        return self.namne

class ApplicationDecision(models.Model):
    Parents = models.ForeignKey(Parents, on_delete=models.CASCADE)
    Schoolprofile = models.ForeignKey(SchoolAdmin, on_delete=models.CASCADE)
    AdmissionForm = models.ForeignKey(AdmissionForm, on_delete=models.CASCADE)
    #status = models.CharField(max_length=20, choices=('Pending', 'Approved', 'Rejected'))

    def __str__(self):
        return self.status
