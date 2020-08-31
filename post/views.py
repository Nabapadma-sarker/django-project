from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from .models import Post,Comment
# Create your views here.

def index(request):
    context = {
        'posts': Post.objects.all()
        }
    return render(request, 'index.html', context)

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