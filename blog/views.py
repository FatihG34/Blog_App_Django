from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from blog.forms import BlogForm, CommentForm
from django.contrib import messages
from blog.models import Comment, Post
from django.shortcuts import get_object_or_404

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
            blog.author = request.user
            blog.save()
            messages.success(request, "Blog created successfully 👏🏻")
            redirect('blog:home')
    context = {
        'form': form
    }
    return render(request, 'blog/post_create.html', context)


@login_required(login_url='login')
def detail(request, slug):
    objct = Post.objects.get(slug=slug)
    context = {
        'post_object': objct
    }
    return render(request, 'blog/detail.html', context)


@login_required(login_url='login')
def update_post(request, slug):
    blogpost = Post.objects.get(slug=slug)
    form = BlogForm(request.POST or None, request.FILES or None, instance=blogpost)
    if form.is_valid():
        form.save()
        return redirect("home")
    context = {
        'blogpost': blogpost,
        'update_form': form
    }
    return render(request, 'blog/post_update.html', context)

def post_delete(request, slug):
    blogpost = get_object_or_404(Post,  slug=slug)
    if request.method == 'POST':
        blogpost.delete()
        return redirect("blog:home")
    context = {
        "blogpost": blogpost
    }
    return render(request, 'blog/post_delete.html', context)


def comment(request,  slug):
    blogpost = Post.objects.get(slug=slug)
    comment_post = Comment.objects.filter(id=blogpost.id)
    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.save()

    context = {
        'blogpost': blogpost,
        'comment_post': comment_post,
        'comment_form': comment_form
    }
    return render(request, 'blog/post_comment.html', context)
