from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    confirmation_code = models.CharField(max_length=6, blank=True, null=True)

    def __str__(self):
        return self.username