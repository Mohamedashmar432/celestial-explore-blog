from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.urls import reverse
import logging
from .models import Post,Category,space_agency
from django.http import Http404
from django.core.paginator import Paginator
from .contact import ContactForm


def index(request):
    blog_title = "Latest post"
    all_post =  Post.objects.order_by('-created_at')[:6]
    all_categories = Category.objects.all()
    all_space_agencies = space_agency.objects.all()
    context = {'blog_title':blog_title,'all_post':all_post,'all_categories': all_categories,'all_space_agencies':all_space_agencies}
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context,request))

def blog(request):
    blog_title = "New post"
    all_post = Post.objects.all()
    all_categories = Category.objects.all()
    all_space_agencies = space_agency.objects.all()
    paginator =  Paginator(all_post,9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context =  {'blog_title': blog_title, 'all_post': all_post, 'all_categories': all_categories,'page_obj': page_obj,'all_space_agencies':all_space_agencies}
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
    #  if request.method == 'POST':
    #     form = ContactForm(request.POST)
    #     name = request.POST.get('name')
    #     email = request.POST.get('email')
    #     message = request.POST.get('message')
        

    #     logger = logging.getLogger("TESTING")
    #     if form.is_valid():
    #         logger.debug(f'POST Data is {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}')
    #         #send email or save in database
    #         success_message = 'Your Email has been sent!'
    #         context =  {'form':form,'success_message':success_message}
    #         return HttpResponse(template.render(context,request)) 
    #     else:
    #         logger.debug('Form validation failure')
    #         context =  {'form':form, 'name': name, 'email':email, 'message': message}
    #     return HttpResponse(template.render(context,request))    
     return HttpResponse(template.render())
