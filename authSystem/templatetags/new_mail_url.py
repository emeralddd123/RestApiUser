from django import template
register = template.Library()

from django.template.defaultfilters import stringfilter


@register.simple_tag(name="make_confirm_url",is_safe=True, takes_context=True)
def make_confirm_url(context):
    activate_url = context.get('activate_url')
    slice_idx = activate_url.find('account')
    return ''.join(['http://frontend.com/email-confirmation', '/',activate_url[slice_idx:]])

