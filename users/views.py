from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout

from users.forms import UserForm

# Create your views here.

def user_login(request):
    form = AuthenticationForm(request, data=request.POST)

    if form.is_valid():
        user = form.get_user()
        if user:
            messages.success(request, "Login successfull")
            login(request, user)
            return redirect('home')
    return render(request, 'users/login.html', {"form": form})


def user_logout(request):
    messages.success(request, "You Logout!")
    logout(request)
    return render(request, 'users/logout.html')

def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        user = form.save()

        login(request, user)
        return redirect('home')
    context = {
        'user_form': form
    }
    return render(request, 'users/register.html', context)