from djongo import models

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length = 50)
    detail = models.TextField(max_length=500)
    def __str__(self):
        return self.name
