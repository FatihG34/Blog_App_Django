from django.shortcuts import render,redirect

from blog.forms import BlogForm

# Create your views here.
def home(request):

    return render(request, 'blog/post_list.html',)

def create_post(request):
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('home')
    context={
        'form': form
    }
    return render(request, 'blog/post_create.html', context)