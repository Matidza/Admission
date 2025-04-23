from django.db import models
from school.models import School
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.apps import apps  # Lazy model lookup


class AdmissionForm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    date_applied = models.DateField(auto_now=True)
    #statuss = models.CharField(max_length=100, blank=False, default='Submitted')
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
    id_number = models.CharField(max_length=13, null=False, blank=False, default='1234567891234', unique=True)



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
    
from django.core.exceptions import ValidationError

class Status(models.Model):
    admissionform = models.OneToOneField(AdmissionForm, on_delete=models.CASCADE, related_name="status")
    APPLICATION_STATUS = [
        ('submitted', 'submitted'),
        ('reviewing', 'reviewing'),
        ('pending', 'pending'),
        ('wait-listed', 'wait-listed'),
        ('rejected', 'rejected'),
        ('admitted', 'admitted'),
    ]
    status = models.CharField(max_length=50, choices=APPLICATION_STATUS, default='submitted')
    reason = models.CharField(max_length=500, blank=True)

    def clean(self):
        if self.status in ['pending', 'wait-listed', 'rejected'] and not self.reason.strip():
            raise ValidationError("Reason is required for pending, wait-listed, or rejected applications.")

    def save(self, *args, **kwargs):
        self.full_clean()  # This will trigger clean()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Status'

    def __str__(self):
        return f"{self.admissionform.childname} - {self.status}"



# Signal to automatically create a Status when an AdmissionForm is created
@receiver(post_save, sender=AdmissionForm)
def create_status(sender, instance, created, **kwargs):
    if created:
        Status.objects.create(admissionform=instance)


    
    