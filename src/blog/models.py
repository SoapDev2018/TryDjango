from django.db import models
from django.conf import settings
from django.utils import timezone

User = settings.AUTH_USER_MODEL

class BlogPostQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(published_date__lte=now)

class BlogPostManager(models.Manager):
    def get_queryset(self):
        return BlogPostQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()

class BlogPost(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    title = models.CharField(max_length=512)
    content = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True)
    published_date = models.DateTimeField('Date Published', auto_now=False, auto_now_add=False, null=True, blank=True)
    timestamp = models.DateTimeField('Timestamp', auto_now_add=True)
    updated = models.DateTimeField('Last Updated', auto_now=True)

    objects = BlogPostManager()

    class Meta:
        ordering = ['-published_date', '-updated', '-timestamp']

    def get_absolute_url(self):
        return f'/blog/{self.slug}'

    def get_edit_url(self):
        return f'/blog/{self.slug}/edit'

    def get_delete_url(self):
        return f'/blog/{self.slug}/delete'