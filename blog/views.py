#encoding=utf8

from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from collections import defaultdict
from math import ceil


# Create your views here.
exclude_posts = ("about", "projects")


def home(request, page=''):
    print "home arg: page :", page
    # 每页显示的数量
    count = 3
    # 传递首页的blog对象
    args = dict()
    # temp = BlogPost.objects.exclude(title__in=exclude_posts)
    args['blogposts'] = BlogPost.objects.exclude(title__in=exclude_posts).order_by('-pub_date')
    # sorted(temp, cmp=lambda x, y: cmp(x.pub_date, y.pub_date), reverse=False)
    # sorted(temp, key=attrgetter('pub_date'), reverse=True)
    # print "after sort ", args['blogposts']
    #samplelist_obj.sort(lambda x,y: cmp(x.a, y.a))

    max_page = int(ceil(len(args['blogposts']) / float(count)))
    print "max_page: ", max_page
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
        # return render(request, '../templates/index.html', args)
        # return HttpResponse("Hello World")


def blogpost(request, slug, id):
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
        # print(""+the_about_post.display_html())
    else:
        print("cannot get about page")

    args = {"about": the_about_post}
    # return render(request, '../templates/about.html', args)
    return render(request, 'about.html', args)



