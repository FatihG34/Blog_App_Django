from dataclasses import fields
from .models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields= '__all__'