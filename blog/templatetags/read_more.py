from django import template
register = template.Library()
# import settings

@register.filter('read_more')
def read_more(body, absolute_url):
    if '<!--more-->' in body:
        return body[:body.find('<!--more-->')]+'<a class="readmore" href="'+str(absolute_url)+'">'+"READ MORE"+'</a>'
    elif '<!-- more -->' in body:
        return body[:body.find('<!-- more -->')]+'<a class="readmore" href="'+str(absolute_url)+'">'+"READ MORE"+'</a>'
    else:
        return body