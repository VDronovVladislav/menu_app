from django import template

from main_menu.models import MenuItem
from menu.settings import PREFIX_URL

register = template.Library()


@register.inclusion_tag("templatetags/menu.html", takes_context=True)
def draw_menu(context, menu_name):
    menu_items = MenuItem.objects.filter(
        menu_name=menu_name, level=1
    ).prefetch_related('children')
    suffix = context['request'].path
    last_part = suffix.split('/')[-2] + '/'
    current_url = PREFIX_URL + suffix
    return {
        "menu_items": menu_items,
        "current_url": current_url,
        "last_part": last_part
    }
