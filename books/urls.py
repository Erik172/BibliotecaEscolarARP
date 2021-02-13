from django.urls import path
from books import views

urlpatterns = [
    path('', views.viewBooks, name='books'),
    path('search', views.searchBook, name='searchBook'),
    path('search/category/<str:category>', views.viewBooksCategory, name='searchBookCategory'),
]