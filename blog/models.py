from django.db import models
from users.models import User
from django.utils.text import slugify

# Create your models here.


class Post(models.Model):
    title = models.CharField('Title', max_length=50)
    content = models.TextField('Content')
    image = models.URLField('Image URL', max_length=200)
    publish_date = models.DateTimeField('Publish Date', auto_now_add=True)
    last_updated = models.DateTimeField('Last Updated Date', auto_now=True)
    status = models.CharField('Status', max_length=50)
    slug = models.SlugField(null=False,unique=True,db_index=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        slugify(self.title + self.user)
        super().save(*args, **kwargs)

class Category(models.Model):
    name= models.CharField('Category Title', max_length=50)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Comment(models.Model):
    content = models.TextField()
    time_stamp = models.DateTimeField('Time, comment added', auto_now_add=False)
    postcomment = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'Added comment at {self.time_stamp} '