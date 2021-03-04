from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import BlogForm
from .models import Blog
from datetime import datetime


"""
def manipulate(prev):
    now = datetime.now()
    diff = prev - now
    return diff
"""


def index(request):
    blogs = Blog.objects.all()
    return render(request, "index.html", { "blogs": blogs})



def create(request):
    form = BlogForm()
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    
    return render(request, "create.html", {"form":form})
    
    
    
def update(request , pk):
    blog = Blog.objects.get(id = pk )
    form = BlogForm( instance = blog  )
    if request.method == "POST":
        form = BlogForm(request.POST,  instance = blog)
        if form.is_valid():
            form.save()
            return redirect ("/")
    
    return render(request, "update.html", {"form":form})
 



def info(request):
    return render(request, "info.html",  {})
    
    
    
def delete (request, pk):
    blog = Blog.objects.get(id = pk)
    if request.method == "POST":
        blog.delete()
        return redirect("/")
    return render (request,  "delete.html",  {"blog" :  blog })