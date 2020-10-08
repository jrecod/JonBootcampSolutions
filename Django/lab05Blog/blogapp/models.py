from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=200)
    image = models.ImageField(upload_to='profile_images/', null=True, blank=True) 
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts') #related name???????
    # public =
    date_created = models.DateTimeField()
    # date_edited = models.DateTimeField()
