from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.urls import reverse
import logging
from .models import Post,Category
from django.http import Http404
from django.core.paginator import Paginator


def index(request):
    blog_title = "Latest post"
    all_post =  Post.objects.order_by('-created_at')[:6]
    all_categories = Category.objects.all()
    context = {'blog_title':blog_title,'all_post':all_post,'all_categories': all_categories}
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context,request))

def blog(request):
    blog_title = "New post"
    all_post = Post.objects.all()
    all_categories = Category.objects.all()
    paginator =  Paginator(all_post,9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context =  {'blog_title': blog_title, 'all_post': all_post, 'all_categories': all_categories,'page_obj': page_obj}
    template = loader.get_template('blog.html')
    return HttpResponse(template.render(context,request))

def blog_details(request,slug):
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:   
         raise Http404("Post Does not Exist!") 
        
        
    template = loader.get_template('blog_content.html')
    context = {'post': post}
    return HttpResponse(template.render(context,request))

def solar_explore(request):
    template = loader.get_template('solar_explore.html')
    return HttpResponse(template.render())

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())
