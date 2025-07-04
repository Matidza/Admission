from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('parent', 'Parent'),
        ('school', 'School'),
    ]
    user_type = models.CharField(max_length=10, choices=ROLE_CHOICES, blank=True)
