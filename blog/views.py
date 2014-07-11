#encoding=utf8

from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from collections import defaultdict
from math import ceil
import datetime

# Create your views here.
exclude_posts = ("about", "projects")


def home(request, page=''):
    # print "home arg: page :", page
    # 每页显示的数量
    count = 3
    # 传递首页的blog对象
    args = dict()
    args['blogposts'] = BlogPost.objects.exclude(title__in=exclude_posts).order_by('-pub_date')
    # Setting max article per page
    max_page = int(ceil(len(args['blogposts']) / float(count)))
    if page and int(page) > max_page:  #0,1 ->/
        #  超出页面 返回首页
        return redirect("/blog")
    else:
        page = int(page) if (page and int(page) > 0) else 1
        args['page'] = page
        # Older
        args['prev_page'] = page+1 if page < max_page else None
        # Newer
        args['next_page'] = page-1 if page > 1 else None
        # slice value
        args['sl'] = str(count*(page-1)) + ":" + str(count*(page-1)+count)
        # print args
        return render(request, 'home.html', args)


def blogpost(request, slug, id):
    blogpost = get_object_or_404(BlogPost, pk=id)
    args = {'blogpost':blogpost}
    return render(request, 'blogpost.html', args)


def blogpost_new(request, year, month, day, slug):
    value = datetime.datetime(int(year), int(month), int(day))

    entry = BlogPost.objects.filter(
        slug=slug,
        pub_date__range=(datetime.datetime.combine(value, datetime.time.min),
                         datetime.datetime.combine(value, datetime.time.max))
    )
    if not entry:
        # TODO raise 404
        print "404"
    else:
        # print(""+ entry)
        args = {'blogpost': entry[0]}
        return render(request, 'blogpost.html', args)


def archive(request):
    args = dict()
    blogposts = BlogPost.objects.exclude(title__in=exclude_posts)

    def get_sorted_posts():
        posts_by_year = defaultdict(list)
        for post in blogposts:
            year = post.pub_date.year
            posts_by_year[year].append(post)
        posts_by_year = sorted(posts_by_year.items(), reverse=True)
        return posts_by_year

    args['posts_by_year'] = get_sorted_posts()
    return render(request, 'archive.html', args)


def about(request):
    # 传递关于页面的对象
    the_about_post = get_object_or_404(BlogPost, title="about")
    if not the_about_post:
        pass
    #     TODO  rasie 404
    args = {"about": the_about_post}
    return render(request, 'about.html', args)


def about_timeline(request):
    return render(request, 'about_timeline.html')



