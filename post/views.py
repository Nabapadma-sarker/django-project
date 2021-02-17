from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Post,Comment
from .forms import CreateForm
from register.logedindecorator import active_user_required
# Create your views here.

@active_user_required
def index(request):
    try:
        posts = Post.objects.filter(author= request.user.username)
        context = {
            'posts': posts
            }
        return render(request, 'post/index.html', context)
    except Post.DoesNotExist:
        return render(request, 'post/index.html', {})

def all(request):
    context = {
        'posts': Post.objects.all()
        }
    return render(request, 'post/index.html', context)

@active_user_required
def create(request):
    if request.method == 'POST':
        post = Post(title= request.POST['post_title'], author= request.user.username, detail= request.POST['post_detail'])
        post.save()
        return redirect('/post/')
    return render(request, 'post/create.html')

@active_user_required
def edit(request, id):
    if request.method == 'POST':
        post = Post.objects.get(id=request.POST['post_id'])
        post.title= request.POST['post_title']
        post.author= request.user.username
        post.detail= request.POST['post_detail']
        post.save() # this will update only
        return redirect('/post/')
    
    
    try:
        context = {
            'post': Post.objects.get(id=id)
        }
    except ObjectDoesNotExist:
        context = {
         'posts':None
        }
    return render(request, 'post/edit.html', context)

def formcreate(request):
    if request.method == 'POST':  
        # Pass the form data to the form class 
        createForm = CreateForm(request.POST) 
  
        # In the 'form' class the clean function  
        # is defined, if all the data is correct  
        # as per the clean function, it returns true 
        if createForm.is_valid():   
  
            # Temporarily make an object to be add some 
            # logic into the data if there is such a need 
            # before writing to the database    
            post = createForm.save(commit = False) 
  
            # Finally write the changes into database 
            post.save()   
  
            # redirect it to some another page indicating data 
            # was inserted successfully 
            return redirect('/post/') 
    form = CreateForm()
    return render(request, 'post/formcreate.html', {'form':form})

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
    return render(request, 'post/detail.html', context)


@active_user_required
def delete(request, id):
    try:
        posts = Post.objects.get(id=id)
        posts.delete()
        return redirect('/post/')
    except ObjectDoesNotExist:
        posts = None
        return render(request, 'post/error.html')