from django.urls import path
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import views
from .loged_in_decorator import is_not_active_user_required

urlpatterns = [
    path('login/', is_not_active_user_required(views.LoginView.as_view( template_name="register/login.html" )), name='login')
]