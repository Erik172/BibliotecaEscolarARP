from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

# Models
from posts.models import Post, Comment

# Forms
from posts.forms import PostForm, CommentForm

# All post view.
def postsList(request):
    posts = Post.objects.all().order_by('-created')
    return render(request, 'posts/posts.html', {'posts': posts})

# Vista para ver un post por su id
def postId(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post, state='Published')

    context = {
        'post': post,
        'comments': comments
    }
    # Filtrar los post Eliminados
    if post.state == 'Delete':
        # Si el usuario es igual al que publico podra ver el post eliminado
        if post.user == request.user:
            return render(request, 'posts/post.html', context)
        
        else:
            return HttpResponse('Publicacion Eliminada', status=401)
    
    return render(request, 'posts/post.html', context)

# View new Post
@login_required
def addPost(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            return redirect('posts')
    context = {
        'form': form
    }

    return render(request, 'posts/new.html', context)

# Vista para Editar Post
@login_required
def editPost(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(instance=post)

    if request.user == post.user:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.save()
                return redirect('posts')
        
        return render(request, 'posts/edit.html', {'post': post, 'form': form})
    else:
        return HttpResponse('No estas autorizado', status=401)

# Vista para Eliminar Post
@login_required
def deletePost(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.user:
        post.state = 'Delete'
        post.save(force_update=True)

        return redirect('home')

# Vista para agregar comentario
# Personas sin registrarse puden cometentar paro despues no lo pueden editar ni eliminar
def addComment(request):
    if request.method == 'POST':
        postPk = request.POST['post']
        post = get_object_or_404(Post, pk=postPk)
        content = request.POST['comment']
        try:
            comment = Comment.objects.create(user=request.user, post=post, content=content)
        except:
            comment = Comment.objects.create(post=post, content=content)
        comment.save()

        return redirect('post', pk=post.pk)

# Vista para editar Comentario
@login_required
def editComment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        # El usuario que publico el post pude editar los comentarios de su post
        if comment.user == request.user or comment.post.user == request.user:
            content = request.POST['comment']
            postPk = request.POST['post']
            comment.content = content
            comment.save(force_update=True)
            return redirect('post', pk=postPk)
        else:
            return HttpResponse('No estas autorizado', status=401)

@login_required
def deleteComment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user == comment.user or comment.post.user == request.user :
        comment.state = 'Delete'
        comment.save(force_update=True)

        return redirect('post', pk=comment.post.pk)

    else:
        return HttpResponse('No estas autorizado', status=401)