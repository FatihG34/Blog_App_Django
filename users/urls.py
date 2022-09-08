from django.urls import path
from users.views import profile, user_login, register, user_logout

urlpatterns = [
    path("login/", user_login, name='login'),
    path("register/", register, name='register'),
    path('logout/', user_logout, name='logout' ),
    path('profile/<int:id>', profile, name='profile' ),
]