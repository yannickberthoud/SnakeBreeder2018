from django import template

from lizard.models import Lizard

register = template.Library()

@register.inclusion_tag('lizard/menu.html')
def lizards_urls():
    lizards = Lizard.objects.order_by("scientific_name")
    return {'lizards': lizards}