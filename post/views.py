from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Post,Comment
# Create your views here.

def index(request):
    context = {
        'posts': Post.objects.all()
        }
    return render(request, 'index.html', context)

def create(request):
    if request.method == 'POST':
        comment = Post(title= request.POST['post_title'], author= request.user.username, detail= request.POST['post_detail'])
        comment.save()
        return redirect('/post/')
    return render(request, 'create.html')

def detail(request, id):
    if request.method == 'POST':
        detailPost = Post.objects.filter(id=id).first()
        comment = Comment(commenter= detailPost.author, comment_detail=request.POST['comment'], post=detailPost)
        comment.save()
    try:
        posts = Post.objects.get(id=id)
    except ObjectDoesNotExist:
        posts = None
    try:
        comments = Comment.objects.filter(post=id)
    except ObjectDoesNotExist:
        comments = None
    context = {
        'post': posts,
        'comment': comments
    }
    return render(request, 'detail.html', context)

def delete(request, id):
    try:
        posts = Post.objects.get(id=id)
        posts.delete()
        return redirect('/post/')
    except ObjectDoesNotExist:
        posts = None
        return render(request, 'error.html')