from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def blog(request):
    template = loader.get_template('blog.html')
    return HttpResponse(template.render())

def blog_details(request,id):
    template = loader.get_template('blog_content.html')
    id = id
    context = {'value': id}
    return HttpResponse(template.render(request,context))

def solar_explore(request):
    template = loader.get_template('solar_explore.html')
    return HttpResponse(template.render())

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())
