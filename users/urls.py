from django.urls import path
from users.views import login

urlpatterns = [
    path("login/", login, name='login'),
]