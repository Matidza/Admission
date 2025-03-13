from django.db import models
from school.models import School
from django.contrib.auth.models import User


class AdmissionForm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    date_applied = models.DateField(auto_now=True)
    status = models.CharField(max_length=100, blank=False, default='Submitted')
    # Child Details / Step 1
    # Tile =
    childname = models.CharField(max_length=100, blank=False)
    childsurname = models.CharField(max_length=100, blank=False)
    # application for which year =
    # grade applying for =
    grade = models.CharField(max_length=100, blank=False, default='')
    parentname = models.CharField(max_length=100, blank=False, default='')
    # Initial =
    # age
    # date of birth
    # Gender
    # Race
    # Nationality 
    # Id/passport Number



    # Parents/ Gurdian
    # Title
    # Name
    # Surname
    # Maiden Nmae
    # Merital Status
    # Initial
    # Race
    # Nationality 
    # Id/passport Number
    # email
    # Celphone number
    # Telephone Number
    # Emergency Contact number
    # Relationship to Child

    # Address same as child's Address
    # Addres 1
    # Address 2
    # Provivence
    # Zip Code

    # Next-of-keen
    # Title
    # Name
    # Surname
    # Initial
    # Maiden Nmae
    # Merital Status
    # Race
    # Nationality 
    # Id/passport Number
    # email
    # Celphone number
    # Telephone Number
    # Emergency Contact number
    # Relationship to Child
    # Relationshiop to parent/gurdian

    # Address same as child's Address
    # Addres 1
    # Address 2
    # Provivence
    # Zip Code





    def save(self, *args, **kwargs):
        if self.user.profile.user_type != 'parent':
            raise ValueError("Only parents can submit admission forms")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.childname
    
