from djongo import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 10)
    detail = models.TextField(max_length=500)
    objects = models.DjongoManager()
    def __str__(self):
        return self.title

class Comment(models.Model):
    commenter = models.CharField(max_length = 10)
    comment_detail = models.TextField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    objects = models.DjongoManager()
    def __str__(self):
        return self.commenter
