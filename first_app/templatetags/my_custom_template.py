from django import template

register = template.Library()

@register.filter(name='bailey_cut')
def bailey_cut(value, arg):
    '''This cuts out all values of arg from the string'''
    return value.replace(arg, '')

