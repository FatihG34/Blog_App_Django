from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from blog.forms import BlogForm, CommentForm
from django.contrib import messages
from blog.models import Comment, Like, Post, Post_view

# Create your views here.


def home(request):
    blogs = Post.objects.filter(status="Published")
    context = {
        'blogs': blogs,
    }
    return render(request, 'blog/post_list.html', context)


@login_required(login_url='users:login')
def create_post(request):
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            messages.success(request, "Blog created successfully 👏🏻")
            return redirect('blog:home')
    context = {
        'form': form
    }
    return render(request, 'blog/post_create.html', context)


@login_required(login_url='users:login')
def detail(request, slug):
    objct = get_object_or_404(Post,  slug=slug)
    form = CommentForm(request.POST or None)
    if request.user.is_authenticated:
        Post_view.objects.get_or_create(user=request.user, post=objct)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.post = objct
        comment.save()
        return redirect("blog:detail", slug=slug)
    context = {
        'post_object': objct,
        "form": form
    }
    return render(request, 'blog/detail.html', context)


@login_required(login_url='users:login')
def update_post(request, slug):
    blogpost = get_object_or_404(Post, slug=slug)
    form = BlogForm(request.POST or None,
                    request.FILES or None, instance=blogpost)
    if form.is_valid():
        form.save()
        return redirect("blog:home")
    context = {
        'blogpost': blogpost,
        'update_form': form
    }
    return render(request, 'blog/post_update.html', context)


@login_required(login_url='users:login')
def post_delete(request, slug):
    blogpost = get_object_or_404(Post,  slug=slug)
    if blogpost.author == request.user:
        if request.method == 'POST':
            blogpost.delete()
            return redirect("blog:home")
    else:
        return redirect("blog:home")
    context = {
        "blogpost": blogpost
    }
    return render(request, 'blog/post_delete.html', context)


@login_required(login_url='users:login')
def like(request, slug):
    if request.method == "POST":
        obj = get_object_or_404(Post, slug=slug)
        like_qs = Like.objects.filter(user=request.user, post=obj)
        if like_qs:
            like_qs[0].delete()
        else:
            Like.objects.create(user=request.user, post=obj)
        return redirect("blog:detail", slug=slug)
