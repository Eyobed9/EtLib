from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    profile_pic = models.ImageField(upload_to="profile_img/", blank=True, null=True)
    role = models.TextField()
    
    def __str__(self):
        return self.username
