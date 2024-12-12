from django.db import models
import datetime
from django.contrib.auth.models import User 

# Create your models here.
class SchoolProfile(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    schoolname = models.CharField(max_length=100 )
    telephone = models.CharField(max_length=200, blank=True)
    schoolemail = models.EmailField(blank=True)
    schooladdress = models.TextField(max_length=100, default="", blank=False)
    postal_address = models.CharField(max_length=100, blank=True)
    '''  
    address1 = models.CharField(max_length=200, blank=True)
    address2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    province = models.CharField(max_length=200, blank=True)
    zipcode = models.CharField(max_length=200, blank=True)'''
    
    website = models.TextField(max_length=100) 
    slogan = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='uploads/schoolprofile/', default=datetime.datetime.today)
    TYPE = [

    ]
    type_of_school = models.CharField(max_length=200, blank=True)
    
    #curriculum
    #grade_levels

    # School Locality
    PROVINCE = [
        ('Limpopo', 'Limpopo'),
        ('Free State', 'Free State'),
        ('Gauteng', 'Gauteng'),
        ('North West', 'North West'),
        ('KZN', 'KZN'),
        ('Mpumalanga', 'Mpumalanga'),
        ('Eastern Cape', 'Eastern Cape'),
        ('Northern Cape', 'Northern Cape'),
        ('Western Cape', 'Western Cape'),
    ]
    province = models.CharField(max_length=20, choices=(PROVINCE))

    DISTRICT = [
        ('Vhembe', 'Vhembe District'),
        ('Free State', 'Free State'),
        ('Gauteng', 'Gauteng'),
    ]
    district = models.CharField(max_length=200,default="",choices=(DISTRICT ))

    CURRICULUM = [

    ]
    curriculum = models.CharField(max_length=100, blank=True)

    GRADES = [

    ]
    grade_levels = models.CharField(max_length=100, blank=True)
    accreditation = models.CharField(max_length=100, blank=True )

    local_municipality = models.CharField(max_length=100)
    urban_rural = models.CharField(max_length=100)
    ward_id = models.CharField(max_length=100)
    Eei_district = models.CharField(max_length=100)


    # SCHOOL IDENTIFICATION
    national_emis_number = models.TextField(max_length=100, blank=True)
    examination_number = models.TextField(max_length=100, blank=True)
    examination_centre = models.TextField(max_length=100, blank=True)
    persal_paypoint_number = models.TextField(max_length=100, blank=True)
    persal_component_number = models.TextField(max_length=100, blank=True)

    
    # Personnel & Staff
    name_of_principal = models.CharField(max_length=100, blank=True)
    number_of_teachers = models.CharField(max_length=100, blank=True )
    number_of_learners = models.CharField(max_length=100, blank=True)

    # School Fees and Finance
    section_21 = models.CharField(max_length=100)
    school_fees = models.CharField(max_length=100)
    QUANTILE = [

    ]
    quintile_Level = models.CharField(max_length=100)


    image = models.ImageField(upload_to='uploads/schoolprofile/', default=datetime.datetime.today)
    image1 = models.ImageField(upload_to='uploads/schoolprofile/', default=datetime.datetime.today)
    image2 = models.ImageField(upload_to='uploads/schoolprofile/', default=datetime.datetime.today)
    image3 = models.ImageField(upload_to='uploads/schoolprofile/', default=datetime.datetime.today)
    image4 = models.ImageField(upload_to='uploads/schoolprofile/', default=datetime.datetime.today)
    image5 = models.ImageField(upload_to='uploads/schoolprofile/', default=datetime.datetime.today)
    image6 = models.ImageField(upload_to='uploads/schoolprofile/', default=datetime.datetime.today)
    
    history = models.CharField(max_length=200, blank=True)
    mission = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.schoolname
    class Meta:
        verbose_name_plural = 'school profile'