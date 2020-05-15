from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

from .forms import ContactForm

from blog.models import BlogPost

def home_page(request):
    my_title = "Welcome to Try Django"
    queryset = BlogPost.objects.published()[:5]
    return render(request, 'home.html', {"title": my_title, "object_list": queryset})

def about_page(request):
    return render(request, 'about.html', {"title": "About Us"})

def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {
        "title": "Contact Us",
        "form": form
    }
    return render(request, 'form.html', context=context)