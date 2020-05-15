from django import forms

from .models import BlogPost


class BlogPostForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)

class DateInput(forms.DateInput):
    input_type = 'date'

class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'image', 'slug', 'content', 'published_date']
        widgets = {
            'published_date': DateInput()
        }

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        instance = self.instance
        qs = BlogPost.objects.filter(title__iexact=title)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise forms.ValidationError("This title has already been used.")
        return title

    def clean_slug(self, *args, **kwargs):
        slug = self.cleaned_data.get('slug')
        if len(slug) < 6:
            raise forms.ValidationError(
                "The slug needs to be at-least 6 characters in length or above")
        if slug.find('-') == -1:
            raise forms.ValidationError(
                "The slug needs to have a '-' character in it.")
        return slug
