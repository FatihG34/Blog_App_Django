from django.urls import path
from blog.views import create_post, home

urlpatterns = [
    path("list/", home, name='home'),
    path("create/", create_post, name='create'),
]