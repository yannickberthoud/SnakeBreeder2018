from django import template

from snake.models import Family, Snake

register = template.Library()

@register.inclusion_tag('snake/menu.html')
def families_urls():
    families = Family.objects.order_by('name')
    return {'families': families}

@register.inclusion_tag('snake/breed.html')
def get_breed(id):
    snakes = Snake.objects.exclude(pk=id).order_by('family', 'scientific_name')[:10]
    return {'snakes': snakes}