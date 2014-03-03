#encoding=utf8

from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import  BlogPost
from collections import defaultdict

# Create your views here.

exclude_posts = ("about", "projects")


def home(request):

    # 传递首页的blog对象
    args = dict()
    args['blogposts'] = BlogPost.objects.exclude(title__in=exclude_posts)
    print args
    return render(request, 'home.html', args)
    # return render(request, '../templates/index.html', args)
    # return HttpResponse("Hello World")


def blogpost(request, id):
    print("model in blogpost method: %s"%id)
    blogpost = get_object_or_404(BlogPost, pk=id)
    args = {'blogpost':blogpost}
    return render(request, 'blogpost.html', args)


def archive(request):
    args = dict()
    blogposts = BlogPost.objects.exclude(title__in=exclude_posts)
    print "archive", blogposts

    def get_sorted_posts():
        posts_by_year = defaultdict(list)
        for post in blogposts:
            year = post.pub_date.year
            posts_by_year[year].append(post)
        # posts_of_a_category = blogposts.filter(category= category)
        # for post in posts_of_a_category:
        #     year = post.pub_date.year
        #     posts_by_year[year].append(post)
        posts_by_year = sorted(posts_by_year.items(), reverse=True)
        return posts_by_year

    # args['data'] = [
    #     ('linux', get_sorted_posts(category='linux')),
    #     ('hello', get_sorted_posts(category='hello')),
    #     ('nc', get_sorted_posts(category='nc')),
    # ]
    args['posts_by_year'] = get_sorted_posts()

    return render(request, 'archive.html', args)


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



