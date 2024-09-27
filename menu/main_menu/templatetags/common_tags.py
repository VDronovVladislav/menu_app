from django import template

from main_menu.models import MenuItem

register = template.Library()


@register.inclusion_tag("templatetags/menu.html", takes_context=True)
def draw_menu(context, menu_name):
    menu_items = MenuItem.objects.filter(
        menu_name=menu_name, level=1
    ).prefetch_related('children')
    return {
        "menu_items": menu_items,
    }
