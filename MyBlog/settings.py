"""
Django settings for MyBlog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

reload(sys)
sys.setdefaultencoding('utf-8')


#
PROJECT_ROOT = os.path.join(
    os.path.realpath(os.path.dirname(__file__)), os.pardir)

# print(">>>>>>>>>>>>>>"+PROJECT_ROOT)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '90)@5$f5sb(iz=w!=w9l5oq21@c&jxr)%(fnc61*4%vq@4u0zb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'xadmin',
    'south',
    'pagedown',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


ROOT_URLCONF = 'MyBlog.urls'


WSGI_APPLICATION = 'MyBlog.wsgi.application'


TEMPLATE_DIRS = (
    # '/Users/shenjie/PycharmProjects/MyBlog/templates',
    os.path.join(PROJECT_ROOT, "blog/templates"),
)


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'blog',    # Or path to database file if using sqlite3.
        'USER': 'root',                    # Not used with sqlite3.
        'PASSWORD': 'hhkb',                # Not used with sqlite3.
        'HOST': 'localhost',        # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',        # Set to empty string for default. Not used with sqlite3.
        }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

#PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

#SITE_ROOT = os.path.join(os.getcwd(), '..')
# SITE_ROOT = "/Users/shenjie/PycharmProjects/MyBlog"
SITE_ROOT = PROJECT_ROOT


# STATIC_ROOT = os.path.join(SITE_ROOT, 'static/')
STATIC_ROOT = ''

STATIC_URL = '/static/'


#STATIC_ROOT = '/Users/shenjie/PycharmProjects/MyBlog/static/'
STATICFILES_DIRS = (
    #("css", os.path.join(STATIC_ROOT, 'css')),
    #("js", os.path.join(STATIC_ROOT, 'js')),
    #("images", os.path.join(STATIC_ROOT, 'img')),
    # os.path.join(SITE_ROOT, 'blog/static'),
    os.path.join(PROJECT_ROOT, 'static/'),
)

#STATICFILES_DIRS = (
# STATICFILES_DIRS = (
    #os.path.join(PROJECT_PATH, 'static/'),
# )
     #'/Users/shenjie/PycharmProjects/MyBlog/static/',
# )

# MEDIA_ROOT = os.path.join(SITE_ROOT, 'media')
# MEDIA_URL = '/media/'
