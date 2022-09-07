from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from blog.forms import BlogForm
from django.contrib import messages

# Create your views here.
def home(request):

    return render(request, 'blog/post_list.html',)

@login_required(login_url='login')
def create_post(request):
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            messages.success(request, "Blog created successfully 👏🏻")
            redirect('home')
    context={
        'form': form
    }
    return render(request, 'blog/post_create.html', context)