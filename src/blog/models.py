from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=512)
    content = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True)
    pub_date = models.DateTimeField('Date Published', auto_now_add=True)