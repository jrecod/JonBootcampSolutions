from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog_category_images/')
    description = models.CharField(blank=True, max_length=200)
    path_name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to='blog_post_images/')
    date_created = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, related_name='blog_posts')
    description = models.CharField(blank=True, max_length=200)

    def __str__(self):
        return self.title
