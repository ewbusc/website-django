# tags.py
# Defines a custom template tag that checks whether the request path matches 
# the pattern. This is used to set the css class of the active tab on the nav 
# bar. The class is 'active'. 
# Source: http://stackoverflow.com/a/477719/6715745
import re
from django import template

register = template.Library()

@register.simple_tag
def active(request, pattern):
    if re.search(pattern, request.path):
        return 'active'
    return ''