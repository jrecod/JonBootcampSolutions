from django.db import models

class ShortenedURL(models.Model):
    url = models.URLField()
    code = models.CharField(max_length=200)
    counter = models.IntegerField()

    def __str__(self):
        return self.code