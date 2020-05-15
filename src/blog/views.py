from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .models import BlogPost
from .forms import BlogPostModelForm


# @login_required
@staff_member_required
def blog_post_create_view(request):
    template_name = 'form.html'
    form = BlogPostModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = BlogPostModelForm()
    context = {'form': form}
    return render(request, template_name, context)


def blog_post_detail_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/detail.html'
    context = {'object': obj}
    return render(request, template_name, context)


def blog_post_list_view(request):
    # Fetch last 5 published blogposts only
    queryset = BlogPost.objects.filter(
        pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
    print(queryset)
    template_name = 'blog/list.html'
    context = {'object_list': queryset}
    return render(request, template_name, context)


@staff_member_required
def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    form = BlogPostModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    template_name = 'form.html'
    context = {'form': form, 'title': f'Update Post {obj.title}'}
    return render(request, template_name, context)


@staff_member_required
def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/delete.html'
    if request.method == "POST":
        obj.delete()
        return redirect('/blog')
    context = {'object': obj}
    return render(request, template_name, context)
