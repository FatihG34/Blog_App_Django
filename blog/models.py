from django.db import models
from users.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField('Title', max_length=50)
    content = models.TextField('Content')
    image = models.URLField('Image URL', max_length=200)
    publish_date = models.DateTimeField('Publish Date', auto_now_add=True)
    last_updated = models.DateTimeField('Last Updated Date', auto_now=True)
    status = models.CharField('Status', max_length=50)
    slug = models.IntegerField('Slug')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
