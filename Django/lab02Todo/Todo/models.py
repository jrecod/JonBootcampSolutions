# Create your models here.
from django.db import models

class TodoItem(models.Model):
    task = models.CharField(max_length=200)
    created_date = models.DateTimeField('date created')
    completed_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.task
