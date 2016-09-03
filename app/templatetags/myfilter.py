from django import template
from django.template.defaultfilters import stringfilter
import markdown2

register = template.Library()

@register.filter
@stringfilter
def mark2html(value):
    return markdown2.markdown(value, extras = { 'code-friendly': 1, 'fenced-code-blocks': { 'cssclass': 'highlight' } })

@register.simple_tag
def url_replace(request, field, value):
    gets = request.GET.copy()
    gets[field] = value
    return gets.urlencode()
