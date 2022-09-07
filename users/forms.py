from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields= ('username', 'email', 'first_name', 'last_name','profile_pic', 'bio')
        labels={
            'username': 'User Name', 
            'first_name':'First Name', 
            'last_name': 'Last Name',
            'email': 'E-mail', 
            'profile_pic' : ' Profile Picture', 
            'bio' : 'Short Biography'
            }

        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control row my-3 mb-3', 'placeholder':'User Name'}), 
            'first_name':forms.TextInput(attrs={'class':'form-control row my-3 mb-3', 'placeholder':'First Name'}), 
            'last_name': forms.TextInput(attrs={'class':'form-control row my-3 mb-3', 'placeholder':'Last Name'}),
            'email': forms.EmailInput(attrs={'class':'form-control row my-3 mb-3', 'placeholder':'E-mail'}),
            'profile_pic' : forms.FileInput(attrs={'class':'form-control row my-3 mb-3'}),
            'bio' :forms.Textarea(attrs={'class':'form-control row mb-3', 'placeholder':'Short Biography', 'rows':6}),
            'password': forms.PasswordInput(attrs={'class':'form-control row mb-3'})
        }