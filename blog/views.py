from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from blog.forms import BlogForm
from django.contrib import messages
from blog.models import Post

# Create your views here.
def home(request):
    blogs = Post.objects.all()
    context = {
        'blogs': blogs,
    }
    return render(request, 'blog/post_list.html', context)

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


@login_required(login_url='login')
def update_post(request,id):
    blogpost = Post.objects.get(id=id)
    form = BlogForm(instance=blogpost)
    if request.method =='POST':
        form = BlogForm(request.POST, instance=blogpost)
        if form.is_valid():
            form.save()
            return redirect("home")
    context={
        'blogpost': blogpost,
        'update_form':form
    }
    return render(request, 'blog/post_update.html', context)

