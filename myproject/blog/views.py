import imp
from time import time, timezone
from django.shortcuts import redirect, render
from .models import Blog
from django.utils import timezone
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    blogs = Blog.objects

    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'home.html', {'blogs':blogs, 'posts':posts})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str (blog.id))

def detail(request, blog_id):
    blog_detail = Blog.objects.get(id=blog_id)
    return render(request, 'detail.html', {'blog':blog_detail})

def delete(request, blog_id):
    Blog.objects.get(id=blog_id).delete()
    return redirect('/')

def edit(request, blog_id):
    blog = Blog.objects.get(id = blog_id)
    return render(request, 'edit.html', {'blog':blog}) 

def update(request, blog_id):
    blog = Blog.objects.get(id = blog_id)
    blog.title = request.POST.get('title')
    blog.body = request.POST.get('body')
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str (blog.id))   




#render는 html파일을 던져주지만 redirect는 url을 던져줌 /는 아무것도 없다?
