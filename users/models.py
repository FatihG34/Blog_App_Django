from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    profile_pic = models.ImageField(
        'Profile Picture', upload_to='profile_pics', default="Avatar.png", blank=True)
    bio = models.TextField('Bio', blank=True)
    