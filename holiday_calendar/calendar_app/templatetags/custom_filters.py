from django import template
from django.template.defaultfilters import stringfilter
import re

register = template.Library()


@register.filter
@stringfilter
def highlight(value, arg):
    return re.sub(
        re.escape(arg),
        '<span class="highlight">\g<0></span>',
        value,
        flags=re.IGNORECASE,
    )
