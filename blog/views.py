#encoding=utf8

from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import  BlogPost

# Create your views here.


def home(request):

    # 传递首页的blog对象
    args = dict()
    # return render(request, '../templates/index.html', args)
    return HttpResponse("Hello World")

def archive(request):

    pass

def about(request):
    # 传递关于页面的对象
    the_about_post = get_object_or_404(BlogPost, title="about")
    if the_about_post:
        print("get about page...")
        print(""+the_about_post.display_html())
    else:
        print("cannot get about page")

    args = {"about": the_about_post}
    # return render(request, '../templates/about.html', args)
    return render(request, 'about.html', args)



