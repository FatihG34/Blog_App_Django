from django.urls import path
from blog.views import comment, create_post, home, update_post

urlpatterns = [
    path('', home,name='home'),
    path("create/", create_post, name='create'),
    path("update/<int:id>", update_post, name='update'),
    path("comment/<int:id>", comment, name='comment'),
]