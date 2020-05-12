from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import BlogPost
from .forms import BlogPostForm

def blog_post_create_view(request):
    template_name = 'blog/create.html'
    form = BlogPostForm(request.POST or None)
    if form.is_valid():
        obj = BlogPost.objects.create(**form.cleaned_data)
        form = BlogPostForm()
    context = {'form': form}
    return render(request, template_name, context)

def blog_post_detail_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/detail.html'
    context = {'object': obj}
    return render(request, template_name, context)

def blog_post_list_view(request):
    # Fetch last 5 published blogposts only
    queryset = BlogPost.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
    print(queryset)
    template_name = 'blog/list.html'
    context = {'object_list': queryset}
    return render(request, template_name, context)

def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/update.html'
    context = {'object': obj, 'form': None}
    return render(request, template_name, context)

def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/delete.html'
    context = {'object': obj}
    return render(request, template_name, context)