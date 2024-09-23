from django import template

from main_menu.models import MenuItem

register = template.Library()


@register.inclusion_tag("templatetags/menu.html", takes_context=True)
def draw_menu(context):
    menu_items = MenuItem.objects.filter(level=1)
    return {
        "menu_items": menu_items,
    }
