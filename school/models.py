from django.db import models
import datetime
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver


# Create School Model containing all
# neccesary fields to create a school profile
class School(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE, 
        # Ensure only school users can be linked
        limit_choices_to={'profile__user_type': 'school'},
        related_name='school_profile',
        null=True,
        blank=True
    )
    schoolname = models.CharField(max_length=100)
    telephone = models.CharField(max_length=200, blank=True)
    schoolemail = models.EmailField(blank=True)
    schooladdress = models.TextField(max_length=100, default="", blank=False)
    postal_address = models.CharField(max_length=100, blank=True)
    website = models.TextField(max_length=100)
    slogan = models.CharField(max_length=200, blank=True)
    image = models.ImageField(
        upload_to='uploads/schoolprofile/', default=None, blank=True, null=True)
    

    SCHOOL_SECTOR = [
        ('Primary', 'Primary School'),
        ('Secondary', 'Secondary School'),
        ('Combined', 'Combined School'),
        ('Vocational', 'Vocational School'),
        ('Other', 'Other School'),
    ]
    type_of_school = models.CharField(
        max_length=200, blank=True, choices=(SCHOOL_SECTOR))

    UMALUSI = [
        ('DBE', 'The Department of Basic Education (DBE)'),
        ('IEB', 'The Independent Examination Board (IEB)'),
        ('SACAI', 'The South African Comprehensive Assessment Institute (SACAI)')
    ]
    umalusi = models.CharField(max_length=200, blank=True, choices=(UMALUSI))

    # School Locality
    PROVINCE = [
        ('Limpopo', 'Limpopo'),
        ('Free State', 'Free State'),
        ('Gauteng', 'Gauteng'),
        ('North West', 'North West'),
        ('KwaZulu-Natal', 'KwaZulu-Natal'),
        ('Mpumalanga', 'Mpumalanga'),
        ('Eastern Cape', 'Eastern Cape'),
        ('Northern Cape', 'Northern Cape'),
        ('Western Cape', 'Western Cape'),
    ]
    provinc = models.CharField(max_length=50, choices=(PROVINCE), null=True)

    DISTRICT = [
        ('Alfred Nzo District', 'Alfred Nzo District'),
        ('amajuba', 'Amajuba District'),
        ('amathole', 'Amathole District'),
        ('bojanala platinum', 'Bojanala Platinum District'),
        ('buffalo city', 'Buffalo City Metropolitan '),
        ('capa winelands', 'Cape Winelands District'),
        ('capricorn', 'Capricorn District'),
        ('central karoo', 'Central Karoo District'),
        ('chris hani', 'Chris Hani District '),
        ('city of cape town', 'City of Cape Town Metropolitan'),
        ('city of johannesburg', 'City of Johannesburg Metropolitan'),
        ('city of tshwane', 'City of Tshwane Metropolitan'),
        ('dr kenneth kaunda', 'Dr Kenneth Kaunda District'),
        ('dr ruth segomotsi mompati', 'Dr Ruth Segomotsi Mompati District '),
        ('ehlanzeni', 'Ehlanzeni District '),
        ('ekurhuleni', 'Ekurhuleni Metropolitan '),
        ('ethekwini', 'eThekwini Metropolitan '),
        ('fezile dabi', 'Fezile Dabi District '),
        ('frances baard', 'Frances Baard District '),
        ('garden route', 'Garden Route District '),
        ('gert sibande', 'Gert Sibande District '),
        ('harry gwala', 'Harry Gwala District '),
        ('ilembe', 'iLembe District'),
        ('joe gqabi', 'Joe Gqabi District'),
        ('john taolo gaetsewe', 'John Taolo Gaetsewe District'),
        ('king cetshwayo', 'King Cetshwayo District '),
        ('lejweleputswa', 'Lejweleputswa District '),
        ('mangaung', 'Mangaung Metropolitan '),
        ('mopani', 'Mopani District'),
        ('namakwa', 'Namakwa District'),
        ('nelson mandela bay', 'Nelson Mandela Bay Metropolitan'),
        ('ngaka modiri molema', 'Ngaka Modiri Molema District '),
        ('nkangala', 'Nkangala District '),
        ('or tambo', 'OR Tambo District '),
        ('overberg', 'Overberg District'),
        ('pixley ka seme', 'Pixley ka Seme District '),
        ('sarah baartman', 'Sarah Baartman District '),
        ('sedibeng', 'Sedibeng District '),
        ('sekhukhune', 'Sekhukhune District'),
        ('thabo mofutsanyana', 'Thabo Mofutsanyana District '),
        ('ugu', 'Ugu District'),
        ('umgungundlovu', 'uMgungundlovu District'),
        ('umkhanyakude', 'uMkhanyakude District '),
        ('umzinyathi', 'uMzinyathi District '),
        ('uthukela', 'uThukela District'),
        ('vhembe', 'Vhembe District'),
        ('waterberg', 'Waterberg District'),
        ('west coast', 'West Coast District '),
        ('west rand', 'West Rand District '),
        ('xhariep', 'Xhariep District '),
        ('zf mgcawu', 'ZF Mgcawu District '),
        ('zululand', 'Zululand District'),







    ]
    district = models.CharField(max_length=200, default="", choices=(DISTRICT))

    CIRCUIT = [
        ('Soutpansberg East', 'Soutpansberg East Circuit'),
        ('Kgakotlou ', 'Kgakotlou '),
        ('Lebowakgomo', 'Lebowakgomo'),
        ('Mankweng ', 'Mankweng '),
        ('Pietersburg ', 'Pietersburg '),
        ('Seshego ', 'Seshego '),
        ('Bochum East ', 'Bochum East '),
        ('Potgietersrus', 'Potgietersrus'),



    ]
    circuit = models.CharField(max_length=200, default="", choices=(CIRCUIT))

    CURRICULUM = [
        ('CAPS', 'CAPS curriculum'),
        ('Cambridge', 'Cambridge curriculum')
    ]
    curriculum = models.CharField(
        max_length=100, blank=True, choices=(CURRICULUM))

    GRADES = [
    ]
    grade_levels = models.CharField(max_length=100, blank=True)
    #accreditation = models.CharField(max_length=100, blank=True)

    local_municipality = models.CharField(max_length=100, blank=True)
    urban_rural = models.CharField(max_length=100, blank=True)
    ward_id = models.CharField(max_length=100, blank=True)
    Eei_district = models.CharField(max_length=100, blank=True)

    # SCHOOL IDENTIFICATION
    emis_number = models.CharField(max_length=100, blank=True)
    examination_number = models.CharField(max_length=100, blank=True)
    examination_centre = models.CharField(max_length=100, blank=True)
    persal_paypoint_number = models.CharField(max_length=100, blank=True)
    persal_component_number = models.CharField(max_length=100, blank=True)

    # Personnel & Staff
    name_of_principal = models.CharField(max_length=100, blank=True)
    number_of_teachers = models.CharField(max_length=100, blank=True)
    #number_of_learners = models.CharField(max_length=100, blank=True)

    # School Fees and Finance
    SECTION = [
        ('Section 21 (Self Reliant)', 'Self Reliant: Yes'),
        ('Section 21 (Self Reliant)', 'Self Reliant: No'),
    ]
    section_21 = models.CharField(max_length=100, choices=(SECTION))
    school_fees = models.CharField(max_length=100)

    QUANTILE = [
        ('Quintile 1', 'Q1'),
        ('Quintile 2', 'Q2'),
        ('Quintile 3', 'Q3'),
        ('Quintile 4', 'Q4'),
        ('Quintile 5', 'Q5'),
    ]
    quintile_Level = models.CharField(max_length=100, choices=(QUANTILE))

    
    image1 = models.ImageField(
        upload_to='uploads/schoolprofile/', default=None, blank=True, null=True)

    history = models.CharField(max_length=200, blank=True)
    mission = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.schoolname

    class Meta:
        verbose_name_plural = 'school profile'


  
class Sports(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=10000, blank=True)
    story = models.TextField(max_length=10000, blank=True)
    date = models.CharField(max_length=10000, blank=True)
    image = models.ImageField(
        upload_to='uploads/sports/', default="", blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Sports'


class Academics(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=10000, blank=True)
    story = models.TextField(max_length=10000, blank=True)
    date = models.CharField(max_length=10000, blank=True)
    image = models.ImageField(
        upload_to='uploads/sports/', default="", blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Academics'