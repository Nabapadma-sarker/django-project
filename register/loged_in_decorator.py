from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from functools import wraps

user_login_required = user_passes_test(lambda user: user.is_active, login_url='login')
def active_user_required(view_func):
    decorated_view_func = login_required(user_login_required(view_func))
    return decorated_view_func

def is_not_active_user_required(view):
    @wraps(view)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_active and request.user.is_authenticated:
            return redirect('/')
        return view(request, *args, **kwargs)
    return _wrapped_view