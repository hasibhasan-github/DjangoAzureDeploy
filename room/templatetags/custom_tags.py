from django import template
from django.utils.safestring import mark_safe
import json

register = template.Library()

@register.filter(name='json_script')
def json_script(value, element_id):
    script_tag = '<script id="{}" type="application/json">{}</script>'.format(
        element_id, json.dumps(value)
    )
    return mark_safe(script_tag)
