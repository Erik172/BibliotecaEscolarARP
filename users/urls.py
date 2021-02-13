from django.urls import path
from users import views

urlpatterns = [
    path('login', views.loginView, name='login'),
    path('logout', views.logoutView, name='logout'),
    path('signup', views.signup, name='signup'),
    path('<str:username>', views.profile, name='profile'),
    path('edit/<str:username>', views.editProfile, name='editProfile'),
]