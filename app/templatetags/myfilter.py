import markdown
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def markdown2html(value):
    return markdown.markdown(value, ['fenced_code', 'tables'])
