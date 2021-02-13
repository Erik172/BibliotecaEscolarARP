from django.contrib import admin
from posts.models import Post, Comment

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'user', 'created', 'modified')
    list_filter = ('title', 'created', 'modified')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'state', 'post', 'content', 'created')
    list_filter = ('created', 'modified', 'state')