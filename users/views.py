from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Models
from django.contrib.auth.models import Group, User
from users.models import Profile
from posts.models import Post

# Forms
from users.form import LoginForm

import os

# Create your views here.
def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'users/login.html', {'error': 'Usuario o Contraseña invalidos'})
    return render(request, 'users/login.html')

@login_required
def logoutView(request):
    logout(request)
    return redirect('login')

# Vista para crear usuario
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        code = request.POST['code']

        if int(code) == 1441:
            try:
                user = User.objects.create_user(username=username, password=password)
            except:
                return render(request, 'users/signup.html', {'error': 'Nombre de usuario ya existe'})

            user.email = email
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            profileU = Profile(user=user)
            profileU.save()

            return redirect('login')  
        else:
            return render(request, 'users/signup.html', {'error': 'Codigo incorrecto'})

    return render(request, 'users/signup.html')

# Vista de usuario
def profile(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(user=user)
    context = {
        'user': user,
        'posts': posts
    }
    return render(request, 'users/profile.html', context)

# Vista para Editar Usario
@login_required
def editProfile(request, username):
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)
    if request.user == user:
        user.email = request.POST['email']
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        profile.description = request.POST['description']
        profile.avatar = request.FILES['avatar']
        profile.save()
        user.save()

        return redirect('profile', username=request.user)
    
    else:
        return HttpResponse('No estas autorizado', status=401)