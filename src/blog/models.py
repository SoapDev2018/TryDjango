from django.db import models

class BlogPost(models.Model):
    title = models.TextField()
    content = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True)