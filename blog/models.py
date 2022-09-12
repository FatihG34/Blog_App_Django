from django.db import models
from users.models import User
from django.utils.text import slugify

# Create your models here.


class Category(models.Model):
    name = models.CharField('Category Title', max_length=100)
    # post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Post(models.Model):
    STATUS = [
        ('Draft', 'Draft'),
        ('Published', 'Published'),
    ]
    title = models.CharField('Title', max_length=50)
    content = models.TextField('Content')
    image = models.URLField('Image URL', max_length=200)
    publish_date = models.DateTimeField('Publish Date', auto_now_add=True)
    last_updated = models.DateTimeField('Last Updated Date', auto_now=True)
    status = models.CharField('Status', max_length=50, choices=STATUS)
    slug = models.SlugField(null=False, unique=True, db_index=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title + " " + self.author.username)
        super().save(*args, **kwargs)
    class Meta:
        verbose_name_plural = "Post"


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.useer.username


class Comment(models.Model):
    content = models.TextField()
    time_stamp = models.DateTimeField( auto_now_add=True)
    postcomment = models.ForeignKey(Post, on_delete=models.CASCADE)
    post_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Added comment by {self.post_user.username}'


class Post_view(models.Model):
    view_time = models.DateTimeField('View Time', auto_now_add=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
