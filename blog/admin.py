#encoding=utf8
from django.contrib import admin

from django import forms
from django.db import models
from django.conf import settings
from .models import BlogPost
from django.forms import TextInput, Textarea
from django.core.files.base import ContentFile
import os
import platform
import codecs
import sys
from pagedown.widgets import AdminPagedownWidget
from .models import Category
from .models import Tag

reload(sys)
sys.setdefaultencoding('utf-8')


# class MyModelForm(forms.ModelForm):
#
#     def __init__(self, *args, **kwargs):
#         print("My Model Form __init__")
#         super(MyModelForm, self).__init__(*args, **kwargs)
#         if self.instance.md_file:
#             self.initial['body'] = self.instance.md_file.read()


class BlogPostModelAdmin(admin.ModelAdmin):
    @staticmethod
    def delete_old_md_file():
        md_file_list = []
        for blogpost in BlogPost.objects.all():
            if blogpost.md_file:
                md_file_list.append(blogpost.filename)

        with open('md_file_list.txt', 'wt') as f:
            f.write(str(md_file_list))

        for root, subdir, files in os.walk(os.path.join(settings.EDIA_ROOT, 'content/BlogPost')):
            for file in files:
                if file not in md_file_list:
                    os.remove(os.path.join(root, file))

    formfield_overrides = {
        # models.CharField: {'widget': TextInput(attrs={'size': '30'})},
        # models.TextField: {'widget': Textarea(attrs={'rows': 100, 'cols': 100})},
        models.TextField: {'widget': AdminPagedownWidget}}

    #Save Action
    def save_model(self, request, obj, form, change):
        # print("save model")
        if obj:
            if obj.body:
                filename = obj.filename()
                # print("====filename is: %s", str(filename))
                # 如果 有文件
                if filename != 'no md file':
                    if platform.system() == 'Windows':
                        pass
                    else:
                        obj.md_file.delete(save=False)
                        obj.html_file.delete(save=False)
                # 没有md file就根据title新建一个
                # print("+++++filename is: %s", str(filename))
                obj.md_file.save(filename + '.md', ContentFile(obj.body), save=False)
                obj.md_file.close()
        obj.save()

    exclude = ('slug',)


#Register to Admin Systm
admin.site.register(BlogPost, BlogPostModelAdmin)
admin.site.register(Category)
admin.site.register(Tag)

