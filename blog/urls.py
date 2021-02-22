"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from post.urls import urlpatterns
from post import views as pv
from register import views as rv, urls as register_url
urlpatterns = [
    path('', pv.all, name="home"),
    path('admin/', admin.site.urls),
    path('post/', include(urlpatterns)),
    path('register/', rv.register, name="register"),
    path('', include(register_url.urlpatterns)),
    path('', include("django.contrib.auth.urls"))
]
