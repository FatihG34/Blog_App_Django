from django.urls import path
from blog.views import home

urlpatterns = [
    path("list/", home, name='home'),
]