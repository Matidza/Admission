from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.apps import apps  # Lazy model lookup
from school.models import School

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(auto_now=True)

    ROLE_CHOICES = [('parent', 'Parent'), ('school', 'School')]
    user_type = models.CharField(max_length=10, choices=ROLE_CHOICES, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'profile'


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # Use get_or_create to avoid IntegrityError if profile already exists
    if created:
        Profile.objects.get_or_create(user=instance)


@receiver(post_save, sender=Profile)
def create_or_delete_school(sender, instance, created, **kwargs):
    # Lazy load the School model to avoid circular imports
    School = apps.get_model('school', 'School')

    if instance.user_type == 'school':
        # Ensure a School instance exists for this user
        School.objects.get_or_create(user=instance.user)
    else:
        # If user is not a school (i.e. parent), delete any associated School instance
        School.objects.filter(user=instance.user).delete()
