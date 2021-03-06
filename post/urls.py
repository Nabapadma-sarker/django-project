from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('create',views.create, name="create"),
    path('edit/<int:id>',views.edit, name="edit"),
    path('form/create',views.formcreate, name="formcreate"),
    path('<int:id>',views.detail, name="detail"),
    path('<int:id>/delete',views.delete, name="delete")
]