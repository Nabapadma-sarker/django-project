from django.shortcuts import render, redirect
from .forms import RegisterForm
# from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = RegisterForm()
        
    return render(request, "register/register.html", {"form": form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            username = request.POST['USERNAME']
            password = request.POST['PASSWORD']
            user = authenticate(username=username, password=password)
            if user is not None : 
                login(request, user)
                return redirect('/')
            else :
                return HttpResponse('Login Failed')
               
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = AuthenticationForm()
        
    return render(request, "register/login.html", {"form": form})

