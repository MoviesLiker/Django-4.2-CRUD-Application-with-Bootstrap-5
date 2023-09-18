from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    created_at = models.DateTimeField("date published")
