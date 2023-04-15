from django import template
from backend.models import Role

register = template.Library()


@register.simple_tag
def roles():
    return Role.objects.all()