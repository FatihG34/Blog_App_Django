from django.urls import path
from blog.views import comment, create_post, home, update_post, detail

app_name='blog'
urlpatterns = [
    path('', home,name='home'),
    path("create/", create_post, name='create'),
    path("<str:slug>/", detail, name='detail'),
    path("<str:slug>/update/", update_post, name='update'),
]