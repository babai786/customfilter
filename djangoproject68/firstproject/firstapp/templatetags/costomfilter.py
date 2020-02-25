from django import template
register=template.Library()


def length(value):
    result=value[0:3]
    return result
register.filter('length',length)
