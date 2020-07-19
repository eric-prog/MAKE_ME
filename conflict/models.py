from django.db import models
from django.contrib.auth.models import User

class Arg(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(blank=True, max_length=100)  
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add = True)
 
    def __str__(self):
        return self.title

class Comment(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(blank=True, max_length=100)  
    date = models.DateTimeField(auto_now_add = True)
    slug = models.SlugField()





