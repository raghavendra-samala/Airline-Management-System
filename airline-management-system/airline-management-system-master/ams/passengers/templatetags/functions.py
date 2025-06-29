from django import template
register = template.Library()

@register.simple_tag()
def division(a,b, *args, **kwargs):
    # returns the fare
    return round(a/b, 3)

@register.simple_tag()
def occu(a,b,c,e,f,g, *args, **kwargs):
    p = (a + b + c) / (e + f + g)
    return round(p, 4)