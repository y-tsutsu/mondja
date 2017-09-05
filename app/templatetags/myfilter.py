from django import template
from django.template.defaultfilters import stringfilter
import markdown

register = template.Library()


@register.filter
@stringfilter
def markdown2html(value):
    return markdown.markdown(value, ['fenced_code', 'tables'])


@register.simple_tag
def url_replace(request, field, value):
    gets = request.GET.copy()
    gets[field] = value
    return gets.urlencode()
