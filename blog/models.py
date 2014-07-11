#encoding=utf8
from django.core.files.base import ContentFile
from django.db import models
from django.utils import timezone
import os
import requests
import markdown
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
import unicodedata
from unidecode import unidecode

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

upload_dir = 'content/BlogPost/%s/%s'


class BlogPost(models.Model):

    STATUS = (('draft', 'published'),
              ('published', 'published'),)

    ## TODO Num of args
    def get_upload_md_name(self, filename):
        year = self.pub_date.year
        upload_to = upload_dir % (year, self.title + '.md')
        return upload_to

    def get_html_name(self, filename):
        year = self.pub_date.year;
        upload_to = upload_dir % (year, filename)
        return upload_to

    #class Meta:
     #   ordering = ['-pub_date']
    title = models.CharField(max_length=150)
    body = models.TextField(blank=True)
    md_file = models.FileField(upload_to=get_upload_md_name, blank=True)
    pub_date = models.DateTimeField('date published', default=timezone.now())
    last_edit_time = models.DateTimeField('last edited', default=timezone.now())
    category = models.CharField(max_length=30)
    tags = models.CharField(max_length=20)
    slug = models.SlugField(max_length=200, blank=True)
    html_file = models.FileField(upload_to=get_html_name, blank=True)
    # status = models.Field(max_length=30, choices=STATUS, default=STATUS[0])

    def filename(self):
        if self.md_file:
            # 获得主文件名
            return os.path.basename(self.title)
        else:
            return 'no md file'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # print("Blog Post is Saving...")
        # self.title.decode(encoding='utf-8')
        # print "Title is %s"%self.title
        # type(self.title)
        self.title = unicode(self.title).decode(encoding='utf-8')
        # print "Title is %s"%self.title
        # self.slug = slugify(unicode(self.title.replace('-', 'and')))
        # if self.pub_date:
            # self.slug = slugify("/" + str(self.pub_date.year) + "/" + str(self.pub_date.month) + "/" + str(self.pub_date.day) + "/"
            #     + unidecode(self.title.replace('-', 'and')))
            # self.slug = "/" + str(self.pub_date.year) + "/" + slugify(unidecode(self.title.replace('-', 'and')))
        # else:
        self.slug = slugify(unidecode(self.title.replace('-', 'and')))
        # print "slug is %s" %self.slug
        # 如果body为空 md file不为空
        if not self.body and self.md_file:
            self.body = self.md_file.read()

        # headers = {'Content-Type': 'text/plain'}

        if self.body:
           self.body.encode('utf-8')
           #转换编码 markdown to html
           r = markdown.markdown(self.body, ['codehilite'])
           # r = requests.post('https://api.github.com/markdown/raw', headers=headers, data=data)
           self.html_file.save(self.title+'.html', ContentFile(r), save=False)
           self.html_file.close()

        models.Model.save(self)

    def display_html(self):
        #TODO encoding is invalid
        with open(self.html_file.path) as f:
        # with open(self.html_file.path, encoding='utf-8') as f:
            return f.read()

    def get_meta_data(self):
        #获取元信息 编辑的时间，作者
        pass

    def get_tags(self):
        return self.tags.encode(encoding='utf-8').split(',')

    def get_absolute_url(self):
        # print "get absolute url,id "
        # print "and then"
        # 对应urls.py中的url.name
        # print ("hello", reverse('blog', kwargs={"id": self.id}))
        # return reverse("blog", kwargs={"slug": self.slug, "id": self.id})
        # return "blog"
        # print(self.pub_date.strftime("%Y/%m/%d"))
        return "%s/%s" % (self.pub_date.strftime("%Y/%m/%d"), self.slug)


class Category(models.Model):
    category = models.CharField(max_length=30)


class Tag(models.Model):
    tag = models.CharField(max_length=30)
