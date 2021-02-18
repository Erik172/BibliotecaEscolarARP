from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from posts.models import Post
from books import services

def home(request):
    posts = Post.objects.all().order_by('-created')
    context = {
        'posts': posts,
        # 'books': services.getMostViewBooks(3, 'spanish')
    }
    return render(request, 'main/index.html', context)