from django.db import models

# Create your models here.

class Node(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    marked = models.BooleanField(default=False)
    trash = models.BooleanField(default=False)

    def __str__(self):
        return self.title