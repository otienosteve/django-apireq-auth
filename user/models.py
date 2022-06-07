
from django.db import models

class Post(models.Model):
    author=models.CharField(max_length=50)
    post=models.TextField()