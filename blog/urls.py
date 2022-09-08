from django.urls import path
from blog.views import create_post, home, update_post

urlpatterns = [
    path('', home,name='home'),
    path("create/", create_post, name='create'),
    path("update/<int:id>", update_post, name='update'),
]