# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'BlogPost.slug'
        db.add_column(u'blog_blogpost', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='', max_length=200, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'BlogPost.slug'
        db.delete_column(u'blog_blogpost', 'slug')


    models = {
        u'blog.blogpost': {
            'Meta': {'object_name': 'BlogPost'},
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'html_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_edit_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 3, 3, 0, 0)'}),
            'md_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 3, 3, 0, 0)'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200', 'blank': 'True'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['blog']