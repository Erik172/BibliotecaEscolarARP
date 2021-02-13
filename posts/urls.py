from django.urls import path
from posts import views

urlpatterns = [
    path('', views.postsList, name='posts'),
    path('<int:pk>', views.postId, name='post'),
    path('edit/<int:pk>', views.editPost, name='editPost'),
    path('edit/comment/<int:pk>', views.editComment, name='editComment'),
    path('delete/<int:pk>', views.deletePost, name='deletePost'),
    path('delete/comment/<int:pk>', views.deleteComment, name='deleteComment'),
    path('new', views.addPost, name='newPost'),
    path('new/comment', views.addComment, name='newComment'),
]