from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    image = models.ImageField(upload_to='posts/image')

    title = models.CharField(max_length=80)
    description = models.CharField(max_length=100, blank=True)
    content = MarkdownxField()

    StateChoices = [
        ('Delete', 'Eliminado'),
        ('Published', 'Publicado')
    ]

    state = models.CharField(max_length=15, choices=StateChoices, default='Published')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    content = models.CharField(max_length=250)

    StateChoices = [
        ('Delete', 'Eliminado'),
        ('Published', 'Publicado')
    ]

    state = models.CharField(max_length=15, choices=StateChoices, default='Published')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

