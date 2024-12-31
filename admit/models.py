from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.apps import apps  # Lazy model lookup
from school.models import School

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(auto_now=True)
    phone = models.CharField(max_length=200, blank=True)
    address1 = models.CharField(max_length=200, blank=True)
    address2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    province = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='uploads/parentprofile/', blank=True, null=True)

    ROLE_CHOICES = [('parent', 'Parent'), ('school', 'School')]
    user_type = models.CharField(max_length=10, choices=ROLE_CHOICES, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'profile'


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=Profile)
def create_school(sender, instance, created, **kwargs):
    if created: # and instance.user_type == 'school':
        # Lazy load the School model to avoid circular imports
        #School = apps.get_model('school', 'School')
        School.objects.create(user=instance.user)
