from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 10)
    detail = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class Comment(models.Model):
    commenter = models.CharField(max_length = 10)
    comment_detail = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    def __str__(self):
        return self.commenter
