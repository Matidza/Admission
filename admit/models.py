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

   
class SchoolProfile(models.Model):
    
    schoolname = models.CharField(max_length=100 )
    telephone = models.CharField(max_length=200, blank=True)
    schoolemail = models.EmailField(blank=True)
    schooladdress = models.TextField(max_length=100, default="", blank=False)
    website = models.CharField(max_length=100 )
    slogan = models.CharField(max_length=200, blank=True)
    type_of_school = models.CharField(max_length=200, blank=True)
    PROVINCE = [
        ('Limpopo', 'Limpopo'),
        ('Free State', 'Free State'),
        ('Gauteng', 'Gauteng'),
    ]
    province = models.CharField(max_length=20, choices=(PROVINCE))

    DISTRICT = [('Vhembe', 'Vhembe'),('Free State', 'Free State'),('Gauteng', 'Gauteng'),]
    district = models.CharField(max_length=200,default="",choices=(DISTRICT ))
    
    curriculum = models.CharField(max_length=100 ,default="")
    grade_levels = models.CharField(max_length=100,default="" )
    accreditationstatus = models.CharField(max_length=100 ,default="")
    
    #date = models.DateField(default=datetime.datetime.today)

    #address1 = models.CharField(max_length=200, blank=True)
    #address2 = models.CharField(max_length=200, blank=True)
    #city = models.CharField(max_length=200, blank=True)
    #province = models.CharField(max_length=200, blank=True)
    #zipcode = models.CharField(max_length=200, blank=True)
    #country = models.CharField(max_length=200, blank=True)
    
 
    image = models.ImageField(upload_to='uploads/schoolprofile/', default=datetime.datetime.today)
    image1 = models.ImageField(upload_to='uploads/schoolprofile/', default=datetime.datetime.today)
    image2 = models.ImageField(upload_to='uploads/schoolprofile/', default=datetime.datetime.today)
    image3 = models.ImageField(upload_to='uploads/schoolprofile/', default=datetime.datetime.today)
    image4 = models.ImageField(upload_to='uploads/schoolprofile/', default=datetime.datetime.today)
    image5 = models.ImageField(upload_to='uploads/schoolprofile/', default=datetime.datetime.today)
    image6 = models.ImageField(upload_to='uploads/schoolprofile/', default=datetime.datetime.today)
    
    

    def __str__(self):
        return self.schoolname
    class Meta:
        verbose_name_plural = 'School Profile'




#class AdmissionFormModel(models.Model):
   # user = models.OneToOneField(User, on_delete=models.CASCADE)
   # childname = models.CharField(max_length=100, blank=False)

  #  def __str__(self):
  #      return self.childname



#class ApplicationStatus(models.Model):
    #admissionformmodel = models.ForeignKey(AdmissionFormModel, on_delete=models.CASCADE)
    #status = models.CharField(max_length=20, choices=('Pending', 'Approved', 'Rejected'))

 #   def __str__(self):
   #     return self.status
