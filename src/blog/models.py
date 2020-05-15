from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class BlogPost(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=512)
    content = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True)
    pub_date = models.DateTimeField('Date Published', auto_now_add=True)

    def get_absolute_url(self):
        return f'{self.slug}'

    def get_edit_url(self):
        return f'{self.slug}/edit'

    def get_delete_url(self):
        return f'{self.slug}/delete'